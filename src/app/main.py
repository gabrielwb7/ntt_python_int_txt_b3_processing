from loguru import logger
from use_cases.extrair_use_case import processar_cotacoes


def main():
    logger.info("Iniciando processamento de cotacoes...")
    processar_cotacoes()
    logger.info("Processamento de cotacoes finalizado.")


if __name__ == "__main__":
    main()
