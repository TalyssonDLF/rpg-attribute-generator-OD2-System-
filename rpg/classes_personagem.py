# rpg/classes_personagem.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List
from .modelos import Personagem

@dataclass
class ClasseBase:
    nome: str
    requisitos: Dict[str, int]
    habilidades: List[str]
    vida_inicial: int

    def validar_requisitos(self, personagem: Personagem) -> bool:
        a = personagem.atributos.como_dict()
        return all(a.get(attr, 0) >= minimo for attr, minimo in self.requisitos.items())

    def aplicar_beneficios(self, personagem: Personagem) -> None:
        if not hasattr(personagem, "habilidades") or personagem.habilidades is None:
            personagem.habilidades = []
        personagem.habilidades.extend(self.habilidades)
        personagem.vida = self.vida_inicial

def criar_classe(nome: str, dados: dict) -> ClasseBase:
    return ClasseBase(
        nome=nome,
        requisitos=dados["requisitos"],
        habilidades=dados["habilidades"],
        vida_inicial=dados["vida_inicial"],
    )
