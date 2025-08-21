from dataclasses import dataclass

@dataclass(frozen=True)
class LivroRegras:

    lados_classico: int = 6
    vezes_classico: int = 3

    lados_aventureiro: int = 6
    vezes_aventureiro: int = 3

    lados_heroico: int = 6