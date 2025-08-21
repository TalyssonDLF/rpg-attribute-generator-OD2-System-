import random
from typing import List

class Dado:
    @staticmethod
    def rolar(lados: int, vezes: int) -> List[int]:
        return [random.randint(1, lados) for _ in range(vezes)]
    
    @staticmethod
    def rolar_soma(lados: int, vezes: int) -> int:
        return sum(Dado.rolar(lados, vezes))
    
    @staticmethod
    def rolar_4d6_drop_lowest() -> int:
        rolagens = Dado.rolar(6, 4)
        rolagens.remove(min(rolagens))
        return sum(rolagens)
                   
    @staticmethod
    def rolar_4d6_descartar_menor() -> int:
        return Dado.rolar_4d6_drop_lowest()                 