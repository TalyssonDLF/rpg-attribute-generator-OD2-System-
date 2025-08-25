# rpg/regras.py
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

ATRIBUTO_MIN = 3
ATRIBUTO_MAX = 18

@dataclass(frozen=True)
class LivroRegras:

    lados_classico: int = 6
    vezes_classico: int = 3

    lados_aventureiro: int = 6
    vezes_aventureiro: int = 3
 
    racas: Dict[str, dict] = field(default_factory=lambda: {
        "HUMANO": {
            "movimento": 9,
            "infravisao": 0,
            "alinhamentos": ("Ordeiro", "Neutro", "Caótico"), 
            "ajustes": {},  
            "habilidades": [
                "Aprendizado: +10% XP",
                "Adaptabilidade: +1 em uma Jogada de Proteção (à escolha)"
            ],
        },
        "ELFO": {
            "movimento": 9,
            "infravisao": 18,
            "alinhamentos": ("Neutro",), 
            "ajustes": {"DES": +2, "CON": -2},
            "habilidades": [
                "Percepção Natural: detectar portas secretas (1 em 1d6; 1–2/1d6 procurando)",
                "Graciosos: +1 em qualquer teste de JPD",
                "Treinamento Racial: +1 dano com arcos",
                "Imunidades: imune a magias de sono e à paralisia de Ghoul",
            ],
        },
        "ANAO": {
            "movimento": 6,
            "infravisao": 18,
            "alinhamentos": ("Ordeiro",),
            "ajustes": {"CON": +2, "CAR": -2},
            "habilidades": [
                "Mineradores: detectar anomalias em pedra (1/1d6; 1–2/1d6 procurando)",
                "Vigoroso: +1 em qualquer teste de JPC",
                "Armas Grandes: restritas (apenas armas pequenas/médias; racial anã conta como média)",
                "Inimigos: ataques contra orcs/ogros/hobgoblins são fáceis",
            ],
        },
        "HALFLING": {
            "movimento": 6,
            "infravisao": 0,
            "alinhamentos": ("Neutro",), 
            "ajustes": {},
            "habilidades": [
                "Furtivos: esconder-se 1–2 em 1d6 (bônus extra se for Ladrão)",
                "Destemidos: +1 em qualquer teste de JPS",
                "Bons de Mira: ataques à distância com arremesso são fáceis",
                "Pequenos: ataques de criaturas grandes+ contra halfling são difíceis",
                "Restrições: usam só couro; armas grandes proibidas (médias contam como 2 mãos)",
            ],
        },
    })

    classes: Dict[str, dict] = field(default_factory=lambda: {
        "GUERREIRO": {
            "requisitos": {"FOR": 9}, 
            "habilidades": [
                "Armas: pode usar todas",
                "Armaduras: pode usar todas",
                "Itens mágicos: não pode usar cajados/varinhas/scrolls (exceto proteção)",
                "Aparar (nível 1)",
                "Maestria em Arma (nível 1; evolui nos níveis 3 e 10)",
                "Ataque Extra (nível 6)",
            ],
            "vida_inicial": 10,
        },
        "CLERIGO": {
            "requisitos": {"SAB": 9},
            "habilidades": [
                "Magias Divinas (preparo diário)",
                "Afastar Mortos-Vivos (nível 1; evolui nos níveis 3 e 10)",
                "Cura Milagrosa: pode trocar magia por Curar Ferimentos (1º círculo; evolui 6 e 10)",
            ],
            "vida_inicial": 8,
        },
        "LADRAO": {
            "requisitos": {"DES": 9},
            "habilidades": [
                "Armas: pequenas/médias; armas grandes tornam ataques difíceis",
                "Armaduras: apenas leves; escudos/armaduras mais pesadas travam habilidades",
                "Itens mágicos: não usam cajados/varinhas/scrolls (exceto proteção)",
                "Ataque Furtivo (x2 no 1º; x3 no 6º; x4 no 10º)",
                "Ouvir Ruídos / Talentos de Ladrão (progressão por nível)",
            ],
            "vida_inicial": 6,
        },
    })
