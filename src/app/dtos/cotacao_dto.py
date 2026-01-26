from datetime import date
from decimal import Decimal


class CotacaoDto:
    
    def __init__(
        self,
        data_pregrao: date,
        cod_bdi: str,
        cod_negociacao: str,
        tipo_mercado: int,
        nome_resumido: str,
        especificacao_papel: str,
        prazo_em_dias: str,
        moeda_ref: str,
        preco_abertura_pregao: Decimal,
        preco_maximo_pregao: Decimal,
        preco_minimo_pregao: Decimal,
        preco_medio_pregao: Decimal,
        preco_ultimo_negociacao_pregao: Decimal,
        preco_melhor_oferta_compra: Decimal,
        preco_melhor_oferta_venda: Decimal,
        total_negocios_pregao: int,
        quantidade_total_titulos_negociados: int,
        volume_total_titulos_negociados: Decimal,
        preco_exercicio: Decimal,
        indicador_correcao_preco_exercicio: int,
        data_vencimento: date,
        fator_cotacao: int,
        preco_exercicio_opcao_ref_dolar: Decimal,
        codigo_isin: str,
        distribuicao_papel: int
    ) {
        self.data_pregrao = data_pregrao
        self.cod_bdi = cod_bdi
        self.cod_negociacao = cod_negociacao
        self.tipo_mercado = tipo_mercado
        self.nome_resumido = nome_resumido
        self.especificacao_papel = especificacao_papel
        self.prazo_em_dias = prazo_em_dias
        self.moeda_ref = moeda_ref
        self.preco_abertura_pregao = preco_abertura_pregao
        self.preco_maximo_pregao = preco_maximo_pregao
        self.preco_minimo_pregao = preco_minimo_pregao
        self.preco_medio_pregao = preco_medio_pregao
        self.preco_ultimo_negociacao_pregao = preco_ultimo_negociacao_pregao
        self.preco_melhor_oferta_compra = preco_melhor_oferta_compra
        self.preco_melhor_oferta_venda = preco_melhor_oferta_venda
        self.total_negocios_pregao = total_negocios_pregao
        self.quantidade_total_titulos_negociados = quantidade_total_titulos_negociados
        self.volume_total_titulos_negociados = volume_total_titulos_negociados
        self.preco_exercicio = preco_exercicio
        self.indicador_correcao_preco_exercicio = indicador_correcao_preco_exercicio
        self.data_vencimento = data_vencimento
        self.fator_cotacao = fator_cotacao
        self.preco_exercicio_opcao_ref_dolar = preco_exercicio_opcao_ref_dolar
        self.codigo_isin = codigo_isin
        self.distribuicao_papel = distribuicao_papel    
    }