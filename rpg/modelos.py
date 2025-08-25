# rpg/modelos.py
from dataclasses import dataclass
from typing import Dict, Tuple

ATRIBUTOS: Tuple[str, ...] = ("FOR", "DES", "CON", "INT", "SAB", "CAR")

@dataclass(frozen=True)
class ConjuntoAtributos:
    FOR: int; 
    DES: int; 
    CON: int; 
    INT: int; 
    SAB: int; 
    CAR: int
    def como_dict(self) -> Dict[str, int]:
        return {k: getattr(self, k) for k in ATRIBUTOS}

@dataclass
class Personagem:
    nome: str
    atributos: ConjuntoAtributos
    classe_escolhida: str | None = None
    raca_escolhida: str | None = None
    alinhamento: str | None = None
    movimento: int | None = None
    infravisao: int | None = None
    habilidades: list[str] | None = None
    vida: int | None = None
