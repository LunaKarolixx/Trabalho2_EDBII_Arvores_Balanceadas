# Sistema de Árvores Balanceadas — AVL e Rubro-Negra

Projeto desenvolvido para a disciplina de Estrutura de Dados com foco na implementação, visualização e análise de desempenho de Árvores Balanceadas.

O sistema permite comparar o funcionamento de:

- Árvore AVL;
- Árvore Rubro-Negra.

---

# Objetivo

Analisar como estruturas balanceadas melhoram o desempenho de operações em comparação com Árvores Binárias de Busca tradicionais.

O projeto realiza:

- Inserção;
- Busca;
- Remoção;
- Comparação de desempenho;
- Visualização gráfica das árvores;
- Demonstração das rotações realizadas.

---

# Funcionalidades

## Árvore AVL
- Inserção;
- Remoção;
- Busca;
- Balanceamento automático;
- Rotações:
  - LL
  - RR
  - LR
  - RL

---

## Árvore Rubro-Negra
- Inserção;
- Remoção;
- Busca;
- Balanceamento automático;
- Recoloração de nós;
- Rotações à esquerda e direita.

---

## Recursos Extras
- Visualização gráfica das árvores com Graphviz;
- Registro automático das rotações realizadas;
- Comparação de desempenho em gráficos;
- Menu interativo no terminal;
- Comparação visual antes e depois das operações (inserção, remoção e busca).

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
```

---

# Tecnologias Utilizadas

- Python
- Graphviz
- Matplotlib
- Google Colab

---

# Como Executar

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

# Testes de Desempenho

O sistema realiza comparações entre:

- Árvore AVL
- Árvore Rubro-Negra

Operações avaliadas:

- Inserção
- Busca
- Remoção

Os resultados são apresentados em gráficos de desempenho gerados automaticamente com Matplotlib.

---

# Visualização das Árvores

As árvores são exportadas automaticamente em imagens `.png`.

Exemplos:

```text
arvore_avl.png
arvore_rubro_negra.png
antes_arvore_avl.png
depois_arvore_avl.png
antes_arvore_rubro_negra.png
depois_arvore_rubro_negra.png
grafico_desempenho.png
```

---

# Balanceamento Automático

O sistema registra automaticamente:

- rotações realizadas;
- recolorações;
- ajustes de balanceamento.

Exemplo:

```text
Rotação simples à direita (LL)
Rotação simples à esquerda (RR)
Rotação dupla à direita (LR)
Rotação dupla à esquerda (RL)
Recoloração dos nós
```

---

# Resultados Observados

Durante os testes realizados:

- A AVL apresentou excelente desempenho em buscas devido ao balanceamento mais rígido.
- A Rubro-Negra apresentou melhor desempenho em inserções e remoções por realizar menos rotações.
- Ambas mantiveram desempenho eficiente mesmo após várias operações.

---

# Conceitos Trabalhados

- Árvores Binárias de Busca
- Balanceamento de Árvores
- Estruturas auto-balanceadas
- Rotação de árvores
- Complexidade de algoritmos
- Análise de desempenho
- Visualização gráfica de estruturas

---

# Equipe

- Luana Karoline de Sousa Oliveira
- Caio Bruno

---

# Projeto no Google Colab

```text
https://colab.research.google.com/drive/1QhCmiZTfmP-YnnMyNcTtHMSe2gH2fNhZ?usp=sharing
```

---

# Passo a Passo para Executar no Google Colab

## 1️. Executar a instalação das bibliotecas

Execute primeiro:

```python
!apt-get install graphviz -y
!pip install graphviz matplotlib
```

---

## 2️. Executar todas as células dos arquivos `.py`

Execute as células na seguinte ordem:

1. `config.py`
2. `avl_tree.py`
3. `red_black_tree.py`
4. `performance.py`
5. `main.py`

---

## 3️. Executar o sistema

Após executar todas as células:

```python
!python main.py
```

---

## 4️. Utilizar o menu do sistema

No menu é possível:

- Inserir elementos
- Remover elementos
- Buscar elementos
- Visualizar árvores
- Executar testes de desempenho

---

## 5️. Gerar as imagens das árvores

Após utilizar as opções de visualização ou realizar operações de inserção/remoção, as imagens `.png` serão geradas automaticamente.

Para visualizar as imagens no Colab, execute:

```python
from IPython.display import Image, display
```

### Exibir AVL

```python
display(Image(filename='arvore_avl.png'))
```

### Exibir Rubro-Negra

```python
display(Image(filename='arvore_rubro_negra.png'))
```

### Exibir imagens antes/depois

```python
display(Image(filename='antes_arvore_avl.png'))
display(Image(filename='depois_arvore_avl.png'))

display(Image(filename='antes_arvore_rubro_negra.png'))
display(Image(filename='depois_arvore_rubro_negra.png'))
```

---

## 6️. Exibir o gráfico de desempenho

Após executar o teste de desempenho:

```python
display(Image(filename='grafico_desempenho.png'))
```

---

# Conclusão

O projeto demonstrou na prática como Árvores Balanceadas melhoram significativamente o desempenho das operações em comparação com árvores binárias tradicionais.

Através dos testes realizados, foi possível observar:

- o impacto do balanceamento automático;
- o funcionamento das rotações;
- as diferenças entre AVL e Rubro-Negra;
- e a eficiência de cada estrutura em diferentes operações.
