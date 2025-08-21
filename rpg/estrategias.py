from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from rpg.dados import Dado
from rpg.modelos import ConjuntoAtributos, ATRIBUTOS
from rpg.regras import Regras

class estrategia(ABC):
    @abstractmethod
    def distribuir(self, regras: Regras) -> ConjuntoAtributos:
        ...

class EstrategiaClassica(estrategia):

    def distribuir(self, regras: Regras) -> ConjuntoAtributos:
        valores = []
        for _ in range(6):
            valores.append(Dado.rolar_soma(regras.lados_classico, regras.vezes_classico))
            mapeamento = {atr: valores[i] for i, atr in enumerate(ATRIBUTOS)}
            return ConjuntoAtributos(**mapeamento)
        
class _DistribuidorInterativo:
    def __init__(self, entrada = input, saida=input):
        self.entrada = entrada
        self.saida = saida

    def atribuir(self, valores: list[int]) -> ConjuntoAtributos:
        pool = valores.copy()
        atribuicoes: dict[str, int] = {}
        self.saida("Distribua os seguintes valores para os atributos:")

        for atributo in ATRIBUTOS:
            while True:
                self.saida(f"Atributo: {atributo}. Disponiveis: {pool}")
                escolha = self.entrada(f"Escolha um valor para {atributo}: ")
                if escolha.isdigit() and int(escolha) in pool:
                    valor = int(escolha)
                    atribuicoes[atributo] = valor
                    pool.remove(valor)
                    break
                else:
                    self.saida("Valor indisponivel. Tente novamente.")  
        return ConjuntoAtributos(**atribuicoes)

class EstrategiaAveintureiro(estrategia):

    def __init__(self, entrada=input, saida=print):
        self.distribuidor = _DistribuidorInterativo(entrada, saida)

    def distribuir(self, regras: Regras) -> ConjuntoAtributos:
        pool = [Dado.rolar_4d6_drop_lowest() for _ in range(6)]
        return self._distribuidor.atribuir(pool)    