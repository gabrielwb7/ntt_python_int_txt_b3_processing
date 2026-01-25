import pytest
from app.readers.parsers.trailer_parser import Trailer


class FakeBaseParser:
    def _extrair(self, txt, inicio, fim):
        return txt[inicio : fim + 1].strip()


class TestTrailerParser(Trailer, FakeBaseParser):
    pass


def test_trailer_valido():
    txt = "99COTAHIST.2025BOVESPA 20251230"

    parser = TestTrailerParser()
    try:
        parser.parser(txt)
    except Exception as e:
        pytest.fail(f"Exception inesperada: {e}")


def test_trailer_tipo_registro_invalido():
    txt = (
        "01"
        "COTAHIST.2023"
        "BOVESPA"
        "20240101"
        + " " * 214
    )

    parser = TestTrailerParser()

    with pytest.raises(ValueError, match="trailer da cotacao invalida"):
        parser.parser(txt)


def test_trailer_origem_invalida():
    txt = (
        "00"
        "COTAHIST.2023"
        "INVALIDO"
        "20240101"
        + " " * 214
    )

    parser = TestTrailerParser()

    with pytest.raises(ValueError):
        parser.parser(txt)


def test_trailer_nome_arquivo_invalido():
    txt = (
        "00"
        "OUTROARQ.2023"
        "BOVESPA"
        "20240101"
        + " " * 214
    )

    parser = TestTrailerParser()

    with pytest.raises(ValueError):
        parser.parser(txt)
