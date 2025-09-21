# 🐖 EcoChiqueiro

Sistema de gerenciamento de informações de porcos e previsão de produção de energia a partir de biogás.

## 📘 Sobre o Projeto

O **EcoChiqueiro** foi criado para auxiliar produtores rurais na organização das informações dos porcos em suas baias e na estimativa da produção de energia a partir do biogás gerado pelos dejetos. Ele permite:

- Cadastro e monitoramento de porcos por baia.
- Cálculo estimado de produção de biogás.
- Comparação entre estimativas e dados reais (se disponíveis).

## 🧰 Requisitos

- Python 3 instalado
- Terminal ou prompt de comando

## 📁 Estrutura dos Arquivos

```
EcoChiqueiro/
├── README.md       # Documentação do projeto
├── calcporc.py     # Cálculo de produção de biogás
├── menu.py         # Menu principal do sistema
├── porccc.py       # Gerenciamento de porcos e baias
```

## ▶️ Como Usar

1. **Clone o repositório:**

```bash
git clone https://github.com/Marianeesouza/EcoChiqueiro.git
cd EcoChiqueiro
```

2. **Execute o sistema:**

```bash
python menu.py
```

3. **Navegue pelo menu interativo:**

O sistema apresenta opções como:

- Cadastrar porcos
- Visualizar baias
- Calcular estimativas de biogás
- Comparar dados reais com estimativas

## 📦 Funcionalidades

### `porccc.py`

- Permite cadastrar porcos com dados como peso, idade e baia.
- Organiza os animais por baia para facilitar o controle.

### `calcporc.py`

- Realiza cálculos de estimativa de produção de biogás com base nos dados dos porcos.
- Pode receber dados reais para gerar relatórios comparativos.

### `menu.py`

- Interface de linha de comando que conecta os módulos.
- Permite navegar entre as funcionalidades de forma simples.

---

Se quiser, posso deixar esse README mais informal, técnico ou até com emojis e estilo visual mais chamativo. Quer que eu personalize?
