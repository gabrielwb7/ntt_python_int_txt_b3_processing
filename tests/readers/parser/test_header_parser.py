import pytest
from app.readers.parsers.header_parser import Header


class FakeBaseParser:
    def _extrair(self, txt, inicio, fim):
        return txt[inicio : fim + 1].strip()


class TestHeaderParser(Header, FakeBaseParser):
    pass


def test_header_valido():
    txt = "00COTAHIST.2025BOVESPA 20251230"

    parser = TestHeaderParser()
    try:
        parser.parser(txt)
    except Exception as e:
        pytest.fail(f"Exception inesperada: {e}")


def test_header_tipo_registro_invalido():
    txt = (
        "01"
        "COTAHIST.2023"
        "BOVESPA"
        "20240101"
        + " " * 214
    )

    parser = TestHeaderParser()

    with pytest.raises(ValueError, match="Header da cotacao invalida"):
        parser.parser(txt)


def test_header_origem_invalida():
    txt = (
        "00"
        "COTAHIST.2023"
        "INVALIDO"
        "20240101"
        + " " * 214
    )

    parser = TestHeaderParser()

    with pytest.raises(ValueError):
        parser.parser(txt)


def test_header_nome_arquivo_invalido():
    txt = (
        "00"
        "OUTROARQ.2023"
        "BOVESPA"
        "20240101"
        + " " * 214
    )

    parser = TestHeaderParser()

    with pytest.raises(ValueError):
        parser.parser(txt)
