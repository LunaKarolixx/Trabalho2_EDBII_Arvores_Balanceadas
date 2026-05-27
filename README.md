# Sistema de Árvores Balanceadas — AVL e Rubro-Negra

Projeto desenvolvido para a disciplina de Estrutura de Dados com foco na implementação e análise de desempenho de Árvores Balanceadas.

O sistema permite comparar o funcionamento de:
- Árvore AVL
- Árvore Rubro-Negra

---

#  Objetivo

Analisar como estruturas balanceadas melhoram o desempenho de operações em comparação com Árvores Binárias de Busca tradicionais.

O projeto realiza:
- Inserção
- Busca
- Remoção
- Balanceamento automático
- Comparação de desempenho
- Visualização gráfica das árvores

---

#  Funcionalidades

## Árvore AVL
- Inserção
- Remoção
- Busca
- Balanceamento automático
- Rotações LL, RR, LR e RL

## Árvore Rubro-Negra
- Inserção
- Remoção
- Busca
- Balanceamento automático
- Recoloração de nós
- Rotações à esquerda e direita

## Recursos Extras
- Visualização gráfica das árvores
- Registro das rotações realizadas
- Comparação de desempenho em gráficos
- Menu interativo no terminal

---

# Estrutura do Projeto

```bash
.
├── avl_tree.py
├── red_black_tree.py
├── performance.py
├── config.py
├── main.py
└── README.md


# Tecnologias Utilizadas

- Python
- Graphviz
- Matplotlib
- Google Colab

---

#  Como Executar

## 1. Instalar dependências

### No computador

```bash
pip install graphviz matplotlib
```

### No Google Colab

```python
!apt-get install graphviz -y
!pip install graphviz matplotlib
```

---

## 2. Executar o sistema

### No terminal

```bash
python main.py
```

### No Google Colab

```python
!python main.py
```

---

#  Testes de Desempenho

O sistema realiza comparações entre:
- Árvore AVL
- Árvore Rubro-Negra

Operações avaliadas:
- Inserção
- Busca
- Remoção

Os resultados são apresentados em gráficos de desempenho gerados automaticamente com Matplotlib.

---

#  Visualização das Árvores

As árvores são exportadas automaticamente em imagens `.png`.

Exemplos:

```text
arvore_avl.png
arvore_rubro_negra.png
antes_arvore_avl.png
depois_arvore_avl.png
```

#  PROJETO NO GOOGLE COLAB: 

```text
https://colab.research.google.com/drive/1QhCmiZTfmP-YnnMyNcTtHMSe2gH2fNhZ?usp=sharing
```
