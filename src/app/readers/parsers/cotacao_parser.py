from loguru import logger
from datetime import date
from decimal import Decimal
from app.readers.base_parser import BaseParser
from app.dtos.cotacao_dto import CotacaoDTO


class Cotacao(BaseParser):

    def parser(self, txt) -> CotacaoDTO:
        tipo_registro = self._extrair(txt, 0, 2)

        valido = self._validar(tipo_registro)

        if not valido: 
            logger.error("Tipo de registro cotacao invalido")
            raise ValueError("Tipo de registro cotacao invalido")

        data_pregrao = datetime.strptime(self._extrair(txt, 2, 10), "%Y%m%d").date()
        codbdi = self._extrair(txt, 10, 12).strip()
        cod_negociacao = self._extrair(txt, 12, 24).strip()
        tipo_mercado = int(self._extrair(txt, 24, 27))
        nome_resumido = self._extrair(txt, 27, 39).strip()
        especificacao_papel = self._extrair(txt, 39, 49).strip()
        prazo_em_dias = self._extrair(txt, 49, 52).strip()
        moeda_ref = self._extrair(txt, 52, 56).strip()
        preco_abertura_pregao = Decimal(self._extrair(txt, 56, 69)) / 100
        preco_maximo_pregao = Decimal(self._extrair(txt, 69, 82)) / 100
        preco_minimo_pregao = Decimal(self._extrair(txt, 82, 95)) / 100
        preco_medio_pregao = Decimal(self._extrair(txt, 95, 108)) / 100
        preco_ultimo_negociacao_pregao = Decimal(self._extrair(txt, 108, 121)) / 100
        preco_melhor_oferta_compra = Decimal(self._extrair(txt, 121, 134)) / 100
        preco_melhor_oferta_venda = Decimal(self._extrair(txt, 134, 147)) / 100
        total_negocios_pregao = int(self._extrair(txt, 147, 152))
        quantidade_total_titulos_negociados = int(self._extrair(txt, 152, 170))
        volume_total_titulos_negociados = Decimal(self._extrair(txt, 170, 188)) / 100
        preco_exercicio = Decimal(self._extrair(txt, 188, 201)) / 100
        indicador_correcao_preco_exercicio = int(self._extrair(txt, 201, 202))
        data_vencimento = datetime.strptime(self._extrair(txt, 202, 210), "%Y%m%d").date()
        fator_cotacao = int(self._extrair(txt, 210, 217))
        preco_exercicio_opcao_ref_dolar = Decimal(self._extrair(txt, 218, 230)) / Decimal("1000000")
        codigo_isin = self._extrair(txt, 230, 242).strip()
        distribuicao_papel = int(self._extrair(txt, 242, 245))

        return CotacaoDTO(
            data_pregrao,
            codbdi,
            cod_negociacao,
            tipo_mercado,
            nome_resumido,
            especificacao_papel,    
            prazo_em_dias,
            moeda_ref,
            preco_abertura_pregao,
            preco_maximo_pregao,
            preco_minimo_pregao,
            preco_medio_pregao,
            preco_ultimo_negociacao_pregao,
            preco_melhor_oferta_compra,
            preco_melhor_oferta_venda,
            total_negocios_pregao,
            quantidade_total_titulos_negociados,
            volume_total_titulos_negociados,
            preco_exercicio,
            indicador_correcao_preco_exercicio,
            data_vencimento,
            fator_cotacao,
            preco_exercicio_opcao_ref_dolar,
            codigo_isin,
            distribuicao_papel
        )

        


    
    def _validar(self, tipo_registro: str) -> bool:
        return tipo_registro == "01"