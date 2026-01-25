from abc import ABC, abstractmethod


class BaseParser(ABC):

    def _extrair(self, txt: str, inicio: int, fim: int) -> str:
        """
        Docstring for _extrair
        
        :param txt: vai receber uma txt de texto no qual vai ser extraido um dado.
        :param inicio: posicao de inicio do dado que vai ser extraido dentro da txt recebida.
        :param fim: posicao final do dado que vai ser extraido dentro da txt recebida.
        :return: retorna dado extraido de forma posicional do txt
        
        """
        return txt[inicio:fim].strip()
    
    
    @abstractmethod
    def parser(self, txt: str):
        pass
