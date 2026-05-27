%%writefile performance.py

import time
import matplotlib.pyplot as plt

from avl_tree import AVLTree
from red_black_tree import RedBlackTree
from config import VALORES_INICIAIS


def medir_tempo(funcao):
    inicio = time.perf_counter()
    funcao()
    fim = time.perf_counter()
    return fim - inicio


def inserir_avl(avl, valores):
    root = None

    for valor in valores:
        root = avl.insert(root, valor)

    return root


def inserir_rb(rb, valores):
    for valor in valores:
        rb.insert(valor)


def buscar_avl(avl, root, valores):
    for valor in valores:
        avl.search(root, valor)


def buscar_rb(rb, valores):
    for valor in valores:
        rb.search(valor)


def remover_avl(avl, root, valores):
    for valor in valores:
        root = avl.delete(root, valor)

    return root


def remover_rb(rb, valores):
    for valor in valores:
        rb.delete(valor)


def testes():

    valores = VALORES_INICIAIS

    avl = AVLTree()
    rb = RedBlackTree()

    tempo_avl_insercao = medir_tempo(
        lambda: inserir_avl(avl, valores)
    )

    avl_root = inserir_avl(avl, valores)

    tempo_rb_insercao = medir_tempo(
        lambda: inserir_rb(rb, valores)
    )

    tempo_avl_busca = medir_tempo(
        lambda: buscar_avl(avl, avl_root, valores)
    )

    tempo_rb_busca = medir_tempo(
        lambda: buscar_rb(rb, valores)
    )

    tempo_avl_remocao = medir_tempo(
        lambda: remover_avl(avl, avl_root, valores)
    )

    tempo_rb_remocao = medir_tempo(
        lambda: remover_rb(rb, valores)
    )

    operacoes = [
        "Inserção",
        "Busca",
        "Remoção"
    ]

    tempos_avl = [
        tempo_avl_insercao,
        tempo_avl_busca,
        tempo_avl_remocao
    ]

    tempos_rb = [
        tempo_rb_insercao,
        tempo_rb_busca,
        tempo_rb_remocao
    ]

    plt.figure(figsize=(8, 5))

    plt.plot(
        operacoes,
        tempos_avl,
        marker="o",
        label="AVL"
    )

    plt.plot(
        operacoes,
        tempos_rb,
        marker="o",
        label="Rubro-Negra"
    )

    plt.title("Comparação de desempenho: AVL x Rubro-Negra")
    plt.xlabel("Operações")
    plt.ylabel("Tempo em segundos")
    plt.legend()
    plt.grid(True)

    plt.savefig("grafico_desempenho.png")
    plt.show()

    print("Gráfico salvo como grafico_desempenho.png")
