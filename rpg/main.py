from __future__ import annotations
import os
import sys
import time
import shutil

from .modelos import Personagem, ConjuntoAtributos
from .regras import LivroRegras
from .estrategias import (
    EstrategiaClassica,
    EstrategiaAventureiro,
    EstrategiaHeroica,
)
from .racas import criar_raca
from .classes_personagem import criar_classe

class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    IT = "\033[3m"
    UL = "\033[4m"

    FG = {
        "gray": "\033[90m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }

    BG = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
    }


def cor(txt: str, *estilos: str) -> str:
    return "".join(estilos) + txt + C.RESET


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def largura_terminal() -> int:
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 80


def centralizar(txt: str) -> str:
    col = largura_terminal()
    return txt.center(col)


def imprimir_lento(txt: str, atraso: float = 0.015):
    for ch in txt:
        print(ch, end="", flush=True)
        time.sleep(atraso)
    print()


def linha(sep: str = "─"):
    col = largura_terminal()
    print(cor(sep * col, C.FG["gray"]))


def moldura(titulo: str | None = None, cor_borda: str = "blue"):
    col = largura_terminal()
    borda = "═"
    topo = "╔" + borda * (col - 2) + "╗"
    base = "╚" + borda * (col - 2) + "╝"
    print(cor(topo, C.FG[cor_borda]))
    if titulo:
        titulo_fmt = f" {titulo} "
        meio = "║" + titulo_fmt.center(col - 2) + "║"
        print(cor(meio, C.FG[cor_borda]))
    print(cor(base, C.FG[cor_borda]))


def banner():
    titulo = r"""
          ╔══════════════════════════════════════════════════════════════╗      
          ║                                                              ║      
          ║                   O L D   D R A G O N   2                    ║      
          ║                                                              ║      
          ║              Crie o seu heroi e comece a jogar               ║      
          ║                                                              ║      
          ╚══════════════════════════════════════════════════════════════╝      
    """.strip("\n")

    for line in titulo.splitlines():
        print(cor(centralizar(line), C.FG["yellow"], C.BOLD))
    subtitulo = "Gerador de Atributos • OD2 System • Python/POO"
    print(cor(centralizar(subtitulo), C.FG["gray"]))
    linha()


def pausa(msg: str = "Pressione ENTER para continuar..."):
    input(cor(f"\n{msg}", C.FG["gray"]))


def animacao_dados(segundos: float = 1.2):
    frames = ["⚄ ⚂", "⚀ ⚅", "⚃ ⚁", "⚂ ⚄", "⚁ ⚃", "⚅ ⚀"]
    t0 = time.time()
    print()
    while time.time() - t0 < segundos:
        for fr in frames:
            print("\r" + cor(f" Rolando dados... {fr} ", C.FG["magenta"], C.BOLD), end="", flush=True)
            time.sleep(0.08)
    print("\r" + " " * 40 + "\r", end="")


def entrada_estilosa(prompt: str) -> str:
    seta = cor("➤", C.FG["cyan"], C.BOLD)
    return input(f"{seta} {cor(prompt, C.FG['white'], C.BOLD)} ")


def saida_estilosa(msg: str):
    print(cor(msg, C.FG["white"]))


# =========================
# Fluxo interativo
# =========================

def escolher_estilo() -> str:
    print(cor("\n Escolha o método de geração (p.14):", C.FG["yellow"], C.BOLD))
    caixa = [
        ("1", "Estilo Clássico", "3d6 em ordem fixa (FOR, DES, CON, INT, SAB, CAR)"),
        ("2", "Estilo Aventureiro", "3d6 seis vezes • você distribui os valores"),
        ("3", "Estilo Heróico", "4d6 descartando o menor • você distribui os valores"),
    ]

    for k, titulo, desc in caixa:
        print(cor(f"\n [{k}] {titulo}", C.FG["cyan"], C.BOLD))
        print(cor(f"     {desc}", C.FG["gray"]))

    while True:
        op = entrada_estilosa("Escolha [1-3]:").strip()
        if op in {"1", "2", "3"}:
            return op
        print(cor(" Opção inválida. Tente novamente.", C.FG["red"], C.BOLD))


def imprimir_atributos(nome_estilo: str, atributos: dict[str, int]):
    linha()
    titulo = f"Atributos ({nome_estilo})"
    print(cor(centralizar(titulo), C.FG["green"], C.BOLD))
    linha()

    ordem = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]
    max_key = max(len(k) for k in ordem)
    for k in ordem:
        v = atributos[k]
        print(centralizar(f"{k:{max_key}} : {v:>2}"))
    linha()


def escolher_raca(regras: LivroRegras, atributos: ConjuntoAtributos):
    # Lista raças do rulebook
    racas_disponiveis = list(regras.racas.keys())
    print(cor("\n Escolha a Raça:", C.FG["yellow"], C.BOLD))
    for i, r in enumerate(racas_disponiveis, 1):
        print(cor(f" [{i}] {r.title()}", C.FG["cyan"]))
    while True:
        op = entrada_estilosa(f"Raça [1-{len(racas_disponiveis)}]:").strip() or "1"
        if op.isdigit() and 1 <= int(op) <= len(racas_disponiveis):
            break
        print(cor(" Opção inválida.", C.FG["red"], C.BOLD))
    nome_raca = racas_disponiveis[int(op) - 1]
    raca = criar_raca(nome_raca, regras.racas[nome_raca])

    # Aplica ajustes raciais fixos (ex.: Elfo +2 DES -2 CON; Anão +2 CON -2 CAR)
    atributos_ajustados = raca.aplicar_ajustes(atributos)

    # Mostra resumo da raça
    linha()
    print(cor(centralizar(f"Raça escolhida: {nome_raca.title()}"), C.FG["green"], C.BOLD))
    print(cor(centralizar(f"Movimento: {raca.movimento} m  •  Infravisão: {raca.infravisao} m"), C.FG["gray"]))
    if raca.habilidades:
        print(cor("\n Habilidades raciais:", C.FG["magenta"], C.BOLD))
        for h in raca.habilidades:
            print("  - " + h)

    # Alinhamento permitido
    print(cor("\n Alinhamentos permitidos:", C.FG["yellow"]))
    for i, a in enumerate(raca.alinhamentos, 1):
        print(f" [{i}] {a}")
    while True:
        op = entrada_estilosa(f"Alinhamento [1-{len(raca.alinhamentos)}]:").strip() or "1"
        if op.isdigit() and 1 <= int(op) <= len(raca.alinhamentos):
            break
        print(cor(" Opção inválida.", C.FG["red"], C.BOLD))
    alinhamento = raca.alinhamentos[int(op) - 1]

    return raca, atributos_ajustados, alinhamento


def escolher_classe(regras: LivroRegras, personagem: Personagem):
    classes_disp = list(regras.classes.keys())
    print(cor("\n Escolha a Classe:", C.FG["yellow"], C.BOLD))
    for i, c in enumerate(classes_disp, 1):
        print(cor(f" [{i}] {c.title()}", C.FG["cyan"]))
    while True:
        op = entrada_estilosa(f"Classe [1-{len(classes_disp)}]:").strip() or "1"
        if op.isdigit() and 1 <= int(op) <= len(classes_disp):
            nome_classe = classes_disp[int(op) - 1]
            break
        print(cor(" Opção inválida.", C.FG["red"], C.BOLD))

    classe = criar_classe(nome_classe, regras.classes[nome_classe])

    # Valida requisitos; se não atender, avisa e volta a escolher
    if not classe.validar_requisitos(personagem):
        print(cor("\n ⚠ Requisitos da classe não atendidos.", C.FG["red"], C.BOLD))
        print(" Requisitos:", classe.requisitos)
        print(" Atributos :", personagem.atributos.como_dict())
        pausa("Pressione ENTER para escolher outra classe...")
        return escolher_classe(regras, personagem)

    # Aplica benefícios (vida inicial + habilidades)
    classe.aplicar_beneficios(personagem)
    return nome_classe


def main():
    limpar_tela()
    banner()

    regras = LivroRegras()
    nome = entrada_estilosa("Nome do personagem:").strip() or "SemNome"

    estilo = escolher_estilo()
    animacao_dados()

    if estilo == "1":
        estrategia = EstrategiaClassica()
        nome_estilo = "Clássico"
    elif estilo == "2":
        estrategia = EstrategiaAventureiro(entrada=entrada_estilosa, saida=saida_estilosa)
        nome_estilo = "Aventureiro"
    else:
        estrategia = EstrategiaHeroica(entrada=entrada_estilosa, saida=saida_estilosa)
        nome_estilo = "Heróico"

    # 1) Atributos
    atributos = estrategia.distribuir(regras)
    imprimir_atributos(nome_estilo, atributos.como_dict())

    # 2) Raça + Alinhamento (aplica ajustes)
    raca, atributos_ajustados, alinhamento = escolher_raca(regras, atributos)

    # 3) Classe (validação de requisitos + benefícios)
    personagem = Personagem(
        nome=nome,
        atributos=atributos_ajustados,
        raca_escolhida=raca.nome.title(),
        alinhamento=alinhamento,
        movimento=raca.movimento,
        infravisao=raca.infravisao,
        habilidades=(raca.habilidades or []).copy(),
    )
    classe_nome = escolher_classe(regras, personagem)
    personagem.classe_escolhida = classe_nome.title()

    # 4) Apresentação final
    limpar_tela()
    banner()
    print(cor(centralizar("PERSONAGEM FORJADO!"), C.FG["green"], C.BOLD))
    linha()
    imprimir_lento(cor(f" Nome  : {personagem.nome}", C.FG["white"], C.BOLD), atraso=0.01)
    imprimir_lento(cor(f" Raça  : {personagem.raca_escolhida}", C.FG["white"], C.BOLD), atraso=0.01)
    imprimir_lento(cor(f" Alinh.: {personagem.alinhamento}", C.FG["white"], C.BOLD), atraso=0.01)
    imprimir_lento(cor(f" Classe: {personagem.classe_escolhida}", C.FG["white"], C.BOLD), atraso=0.01)
    imprimir_lento(cor(f" Vida  : {personagem.vida}", C.FG["white"], C.BOLD), atraso=0.01)
    print()
    for k, v in personagem.atributos.como_dict().items():
        imprimir_lento(cor(f"  {k}: {v}", C.FG["cyan"], C.BOLD), atraso=0.01)

    if personagem.habilidades:
        linha()
        print(cor(centralizar("Habilidades"), C.FG["magenta"], C.BOLD))
        for h in personagem.habilidades:
            imprimir_lento(cor(f" • {h}", C.FG["magenta"]), atraso=0.01)

    linha()
    imprimir_lento(cor("Que os dados sorriam para você nas próximas jornadas!", C.FG["magenta"], C.IT), atraso=0.01)
    print()

    # 5) Salvar ficha em JSON
    resp = entrada_estilosa("Deseja salvar a ficha em JSON? [s/N]").lower().strip()
    if resp == "s":
        import json
        nome_arquivo = f"{personagem.nome.replace(' ', '_')}.json"
        with open(nome_arquivo, "w", encoding="utf-8") as arq:
            json.dump(
                {
                    "nome": personagem.nome,
                    "raca": personagem.raca_escolhida,
                    "alinhamento": personagem.alinhamento,
                    "classe": personagem.classe_escolhida,
                    "vida": personagem.vida,
                    "habilidades": personagem.habilidades,
                    "atributos": personagem.atributos.como_dict(),
                    "metodo_atributos": nome_estilo,
                },
                arq,
                ensure_ascii=False,
                indent=2,
            )
        print(cor(f"\n Ficha salva em {nome_arquivo}", C.FG["green"], C.BOLD))
    print()
    pausa("Pressione ENTER para encerrar...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + cor("Saindo do salão da guilda...", C.FG["gray"]))
