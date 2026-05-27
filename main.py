%%writefile main.py

from avl_tree import AVLTree
from red_black_tree import RedBlackTree
from performance import testes
from config import VALORES_INICIAIS


def criar_arvore(escolha):
    if escolha == "1":
        arvore = AVLTree()
        nome = "AVL"
        root = None

        for valor in VALORES_INICIAIS:
            root = arvore.insert(root, valor)

        return arvore, nome, root

    elif escolha == "2":
        arvore = RedBlackTree()
        nome = "Rubro-Negra"
        root = None

        for valor in VALORES_INICIAIS:
            arvore.insert(valor)

        return arvore, nome, root

    return None, None, None


def visualizar(arvore, nome, root, nome_arquivo):
    if nome == "AVL":
        imagem = arvore.visualize(root)
    else:
        imagem = arvore.visualize()

    imagem.render(nome_arquivo, format="png", cleanup=True)
    print(f"Imagem salva como {nome_arquivo}.png")


def mostrar_ajustes(arvore, nome):
    if nome == "AVL":
        ajustes = arvore.rotacoes
    else:
        ajustes = arvore.adjustments

    if ajustes:
        print("Rotações/ajustes realizados:")
        for ajuste in ajustes:
            print("-", ajuste)
    else:
        print("Não foi necessário rotação!")


def escolher_arvore():
    print("===================================")
    print(" SISTEMA DE ÁRVORES BALANCEADAS")
    print("===================================")
    print("1 - Árvore AVL")
    print("2 - Árvore Rubro-Negra")
    print("0 - Sair")

    escolha = input("Escolha a árvore: ")

    if escolha == "0":
        return None, None, None

    arvore, nome, root = criar_arvore(escolha)

    if arvore is None:
        print("Opção inválida!")
        return escolher_arvore()

    print("\nValores iniciais inseridos:")
    print(VALORES_INICIAIS)

    return arvore, nome, root


def main():

    while True:

        arvore, nome, root = escolher_arvore()

        if arvore is None:
            print("Programa finalizado.")
            break

        while True:

            print("\n===== MENU =====")
            print("Árvore escolhida:", nome)
            print("1 - Inserir")
            print("2 - Remover")
            print("3 - Buscar")
            print("4 - Mostrar em ordem")
            print("5 - Visualizar")
            print("6 - Teste de desempenho")
            print("7 - Voltar para escolher outra árvore")
            print("0 - Sair")

            opcao = input("Opção: ")

            if opcao == "1":
                valor = int(input("Valor para inserir: "))

                print("\nAntes da inserção:")

                if nome == "AVL":
                    visualizar(arvore, nome, root, "antes_arvore_avl")
                    arvore.rotacoes.clear()
                    root = arvore.insert(root, valor)
                    visualizar(arvore, nome, root, "depois_arvore_avl")
                else:
                    visualizar(arvore, nome, root, "antes_arvore_rubro_negra")
                    arvore.adjustments.clear()
                    arvore.insert(valor)
                    visualizar(arvore, nome, root, "depois_arvore_rubro_negra")

                print("\nDepois da inserção:")
                mostrar_ajustes(arvore, nome)

            elif opcao == "2":
                valor = int(input("Valor para remover: "))

                print("\nAntes da remoção:")

                if nome == "AVL":
                    visualizar(arvore, nome, root, "antes_remocao_avl")
                    arvore.rotacoes.clear()
                    root = arvore.delete(root, valor)
                    visualizar(arvore, nome, root, "depois_remocao_avl")
                else:
                    visualizar(arvore, nome, root, "antes_remocao_rubro_negra")
                    arvore.adjustments.clear()
                    arvore.delete(valor)
                    visualizar(arvore, nome, root, "depois_remocao_rubro_negra")

                print("\nDepois da remoção:")
                mostrar_ajustes(arvore, nome)

            elif opcao == "3":
                valor = int(input("Valor para buscar: "))

                if nome == "AVL":
                    resultado = arvore.search(root, valor)
                else:
                    resultado = arvore.search(valor)

                if resultado is not None:
                    print("Elemento encontrado!")
                else:
                    print("Elemento não encontrado!")

            elif opcao == "4":
                print("\nValores em ordem:")

                if nome == "AVL":
                    arvore.inorder(root)
                    print()
                else:
                    arvore.show_in_order()

            elif opcao == "5":
                if nome == "AVL":
                    visualizar(arvore, nome, root, "arvore_avl")
                else:
                    visualizar(arvore, nome, root, "arvore_rubro_negra")

            elif opcao == "6":
                testes()

            elif opcao == "7":
                print("\nVoltando para escolher outra árvore...")
                break

            elif opcao == "0":
                print("Programa finalizado.")
                return

            else:
                print("Opção inválida!")


main()
