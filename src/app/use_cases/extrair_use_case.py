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


def salvar_cotacao(db: Session, cotacao_dto: CotacaoDto) -> None:
    cotacao_model = cotacao_dto.para_cotacao_model()
    db.add(cotacao_model)


def processar_cotacoes(batch=1000) -> None:
    buffer = 0

    with SessionLocal() as db:
        with arquivo.open("r") as file:
            for line in file:
                tipo_registro = line[0:2]

                if tipo_registro == "00":
                    header = Header()
                    header_data = header.parser(line)
                    logger.info(f"Header Processado: {header_data}")

                elif tipo_registro == "01":
                    cotacao = Cotacao()
                    cotacao_data = cotacao.parser(line)
                    salvar_cotacao(db, cotacao_data)
                    buffer += 1

                    if buffer >= batch:
                        db.commit()
                        buffer = 0

                    logger.info(f"Cotacao Processada: {cotacao_data}")

                elif tipo_registro == "99":
                    trailer = Trailer()
                    trailer_data = trailer.parser(line)
                    logger.info(f"Trailer Processado: {trailer_data}")
    db.commit()
