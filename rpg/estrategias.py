from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from rpg.dados import Dado
from rpg.modelos import ConjuntoAtributos, ATRIBUTOS
from rpg.regras import LivroRegras


class estrategia(ABC):
    @abstractmethod
    def distribuir(self, regras: LivroRegras) -> ConjuntoAtributos:
        ...


class EstrategiaClassica(estrategia):

    def distribuir(self, regras: LivroRegras) -> ConjuntoAtributos:
        valores: List[int] = [
            Dado.rolar_soma(regras.lados_classico, regras.vezes_classico)
            for _ in range(6)
        ]
        mapeamento = {atr: valores[i] for i, atr in enumerate(ATRIBUTOS)}
        return ConjuntoAtributos(**mapeamento)


class _DistribuidorInterativo:
    def __init__(self, entrada=input, saida=print):
        self.entrada = entrada
        self.saida = saida

    def atribuir(self, valores: list[int]) -> ConjuntoAtributos:
        pool = valores.copy()
        atribuicoes: dict[str, int] = {}
        self.saida("Distribua os seguintes valores para os atributos:")

        for atributo in ATRIBUTOS:
            while True:
                self.saida(f"Atributo: {atributo}. Disponíveis: {pool}")
                escolha = self.entrada(f"Escolha um valor para {atributo}: ")
                if escolha.isdigit() and int(escolha) in pool:
                    valor = int(escolha)
                    atribuicoes[atributo] = valor
                    pool.remove(valor)
                    break
                else:
                    self.saida("Valor indisponível. Tente novamente.")
        return ConjuntoAtributos(**atribuicoes)


class EstrategiaAventureiro(estrategia):

    def __init__(self, entrada=input, saida=print):
        self._distribuidor = _DistribuidorInterativo(entrada, saida)

    def distribuir(self, regras: LivroRegras) -> ConjuntoAtributos:
        pool = [
            Dado.rolar_soma(regras.lados_aventureiro, regras.vezes_aventureiro)
            for _ in range(6)
        ]
        return self._distribuidor.atribuir(pool)


class EstrategiaHeroica(estrategia):

    def __init__(self, entrada=input, saida=print):
        self._distribuidor = _DistribuidorInterativo(entrada, saida)

    def distribuir(self, regras: LivroRegras) -> ConjuntoAtributos:
        pool = [Dado.rolar_4d6_descartar_menor() for _ in range(6)]
        return self._distribuidor.atribuir(pool)