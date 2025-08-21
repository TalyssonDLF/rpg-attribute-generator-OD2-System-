from dataclasses import dataclass
from typing import List, Optional, Tuple

ATRIBUTOS: Tuple[str, ...] = ("FOR", "DES", "CON", "INT", "SAB", "CAR")

@dataclass(frozen=True)
class ConjuntoAtributos:
    FOR: int
    DES: int
    CON: int
    INT: int
    SAB: int
    CAR: int

    def como_dict(self) -> dict[str, int]:
        return {atributo: getattr(self, atributo) for atributo in ATRIBUTOS}
    
@dataclass
class Personagem:
    nome: str
    atributos: ConjuntoAtributos
    classe_escolhida: str | None = None    