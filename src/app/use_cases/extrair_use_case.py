from loguru import logger
from readers.parsers.cotacao_parser import Cotacao
from readers.parsers.header_parser import Header
from readers.parsers.trailer_parser import Trailer
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]
arquivo = BASE_DIR / "data" / "raw" / "COTAHIST_A2025.TXT"

def processar_cotacoes():

    with arquivo.open('r') as file:
        for line in file:
            tipo_registro = line[0:2]

            if tipo_registro == '00':
                header = Header()
                header_data = header.parser(line)
                logger.info(f"Header Processado: {header_data}")

            elif tipo_registro == '01':
                cotacao = Cotacao()
                cotacao_data = cotacao.parser(line)
                logger.info(f"Cotacao Processada: {cotacao_data}")

            elif tipo_registro == '99':
                trailer = Trailer()
                trailer_data = trailer.parser(line)
                logger.info(f"Trailer Processado: {trailer_data}")