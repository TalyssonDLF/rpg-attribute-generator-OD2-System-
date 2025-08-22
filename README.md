# RPG Attribute Generator (OD2 System)

Projeto desenvolvido para a disciplina **Tópicos Especiais em Software**, utilizando **Python** e **Programação Orientada a Objetos (POO)**.  
O sistema implementa a geração de atributos de personagens de RPG conforme o **Old Dragon 2 (OD2)**, página 14 do livro de regras.

---

## Funcionalidades

- Geração de atributos de personagem em **três estilos**:
  - **Estilo Clássico** → Rola `3d6` seis vezes e atribui em ordem fixa: **FOR, DES, CON, INT, SAB, CAR**.
  - **Estilo Aventureiro** → Rola `3d6` seis vezes e o **jogador distribui** livremente os valores.
  - **Estilo Heróico** → Rola `4d6` descartando o menor, seis vezes, e o **jogador distribui** livremente os valores.
- Interação no terminal **estilizada**, com menus e prompts imersivos.
- Escolha da **classe do personagem** após definir atributos.
- Opção para **salvar a ficha em JSON**.
- Código estruturado em **POO** com separação clara de responsabilidades.

---

## 🛠 Estrutura do Projeto
rpg-attribute-generator-od2/
│
├── rpg/
│   ├── init.py
│   ├── principal.py        # Arquivo principal (entrypoint do sistema)
│   ├── dados.py            # Classe Dado (rolagens de dados)
│   ├── modelos.py          # Modelos: ConjuntoAtributos, Personagem
│   ├── estrategias.py      # Estratégias de distribuição (Clássico, Aventureiro, Heróico)
│   └── regras.py           # Parâmetros do livro de regras
│
└── README.md               # Este arquivo


---

## Como Executar

### Pré-requisitos
- **Python 3.10+** instalado
- Terminal com suporte a **ANSI colors** (Linux/macOS já suportam; no Windows use o Windows Terminal ou VSCode)

### Rodando o projeto

Dentro da pasta **pai de `rpg/`**, execute:

```bash
python3 -m rpg.principal

