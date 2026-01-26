from sqlalchemy import \
    Column, Integer, String, Decimal, ForeignKey
from app.database.bd import Base


class CotacaoModel(Base):
    __tablename__ = "cotacoes"

    id = Column(Integer, primary_key=True, index=True)
    data_pregrao = Column(String, nullable=False)
    cod_bdi = Column(String, nullable=False)
    cod_negociacao = Column(String, nullable=False)
    tipo_mercado = Column(Integer, nullable=False)
    nome_resumido = Column(String, nullable=False)
    especificacao_papel = Column(String, nullable=False)
    prazo_em_dias = Column(String, nullable=False)
    moeda_ref = Column(String, nullable=False)
    preco_abertura_pregao = Column(Decimal, nullable=False)
    preco_maximo_pregao = Column(Decimal, nullable=False)
    preco_minimo_pregao = Column(Decimal, nullable=False)
    preco_medio_pregao = Column(Decimal, nullable=False)
    preco_ultimo_negociacao_pregao = Column(Decimal, nullable=False)
    preco_melhor_oferta_compra = Column(Decimal, nullable=False)
    preco_melhor_oferta_venda = Column(Decimal, nullable=False)
    total_negocios_pregao = Column(Integer, nullable=False)
    quantidade_total_titulos_negociados = Column(Integer, nullable=False)
    volume_total_titulos_negociados = Column(Decimal, nullable=False)
    preco_exercicio = Column(Decimal, nullable=False)
    indicador_correcao_preco_exercicio = Column(Integer, nullable=False)
    data_vencimento = Column(String, nullable=False)
    fator_cotacao = Column(Integer, nullable=False)
    preco_exercicio_opcao_ref_dolar = Column(Decimal, nullable=False)
    codigo_isin = Column(String, nullable=False)
    distribuicao_papel = Column(Integer, nullable=False)
