from loguru import logger
from pathlib import Path
from sqlalchemy.orm import Session
from database.bd import SessionLocal, engine
from dtos.cotacao_dto import CotacaoDto
from models import cotacao_model
from readers.parsers.cotacao_parser import Cotacao
from readers.parsers.header_parser import Header
from readers.parsers.trailer_parser import Trailer


BASE_DIR = Path(__file__).resolve().parents[3]
arquivo = BASE_DIR / "data" / "raw" / "COTAHIST_A2025.TXT"

cotacao_model.Base.metadata.create_all(bind=engine)


def processar_cotacoes(batch_size: int = 1000) -> None:
    """Processa cotações com otimização de batch para melhor performance."""
    logger.info("Iniciando o processamento de cotações...")
    
    header = Header()
    trailer = Trailer()
    cotacao = Cotacao()
    
    cotacoes_buffer = []
    total_processado = 0

    with SessionLocal() as db:
        with arquivo.open("r") as file:
            for line in file:
                tipo_registro = line[0:2]

                if tipo_registro == "00":
                    header_data = header.parser(line)

                elif tipo_registro == "01":
                    cotacao_data = cotacao.parser(line)
                    cotacao_model = cotacao_data.para_cotacao_model()
                    cotacoes_buffer.append(cotacao_model)
                    
                    # Commit em lotes para melhor performance
                    if len(cotacoes_buffer) >= batch_size:
                        db.bulk_save_objects(cotacoes_buffer)
                        db.commit()
                        total_processado += len(cotacoes_buffer)
                        logger.info(f"Processados {total_processado} registros...")
                        cotacoes_buffer = []

                elif tipo_registro == "99":
                    trailer_data = trailer.parser(line)
        
        # Commit dos registros restantes
        if cotacoes_buffer:
            db.bulk_save_objects(cotacoes_buffer)
            db.commit()
            total_processado += len(cotacoes_buffer)
            logger.info(f"Processados {total_processado} registros...")

    logger.info(f"Processamento de cotações concluído. Total: {total_processado} registros.")