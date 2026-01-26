from loguru import logger
from readers.base_parser import BaseParser


class Header(BaseParser):

    def parser(self, txt):
        tipo_registro = self._extrair(txt, 0, 2)
        nome_arquivo = self._extrair(txt, 2, 15)
        origem = self._extrair(txt, 15, 22)
        data_geracao = self._extrair(txt, 22, 30)

        valido = self._validar(tipo_registro, nome_arquivo, origem)

        if not valido: 
            logger.error("Erro ao validar campos do header do txt da cotacao")
            raise ValueError("Header da cotacao invalida")
        
        logger.info(f"header validado com sucesso, cotacao {nome_arquivo} gerada na data {data_geracao}")


    
    def _validar(self, tipo_registro: str, nome_arquivo: str, origem: str) -> bool:
        tipo_registro_valido = tipo_registro == "00"
        nome_arquivo_valido = nome_arquivo.startswith("COTAHIST")
        origem_valida = origem == "BOVESPA"

        return tipo_registro_valido and origem_valida and nome_arquivo_valido