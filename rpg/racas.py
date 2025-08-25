# rpg/racas.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from .modelos import ConjuntoAtributos, ATRIBUTOS
from .regras import ATRIBUTO_MIN, ATRIBUTO_MAX

def _clamp(x: int) -> int:
    return max(ATRIBUTO_MIN, min(ATRIBUTO_MAX, x))

@dataclass
class Raca:
    nome: str
    movimento: int
    infravisao: int
    alinhamentos: Tuple[str, ...]
    habilidades: List[str] = field(default_factory=list)
    ajustes: Dict[str, int] = field(default_factory=dict)

    def aplicar_ajustes(self, base: ConjuntoAtributos) -> ConjuntoAtributos:
        d = base.como_dict()
        for k, mod in self.ajustes.items():
            if k in d:
                d[k] = _clamp(d[k] + mod)
        return ConjuntoAtributos(**d)

def criar_raca(nome: str, dados: dict) -> Raca:
    return Raca(
        nome=nome,
        movimento=dados["movimento"],
        infravisao=dados["infravisao"],
        alinhamentos=tuple(dados["alinhamentos"]),
        habilidades=list(dados.get("habilidades", [])),
        ajustes=dict(dados.get("ajustes", {})),
    )
