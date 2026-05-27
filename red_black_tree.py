%%writefile red_black_tree.py

from graphviz import Digraph


class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = "BLACK"
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = None

        self.root = self.NIL
        self.adjustments = []

    def rotate_left(self, node):
        self.adjustments.append("Rotação simples à esquerda")

        aux = node.right
        node.right = aux.left

        if aux.left != self.NIL:
            aux.left.parent = node

        aux.parent = node.parent

        if node.parent is None:
            self.root = aux
        elif node == node.parent.left:
            node.parent.left = aux
        else:
            node.parent.right = aux

        aux.left = node
        node.parent = aux

    def rotate_right(self, node):
        self.adjustments.append("Rotação simples à direita")

        aux = node.left
        node.left = aux.right

        if aux.right != self.NIL:
            aux.right.parent = node

        aux.parent = node.parent

        if node.parent is None:
            self.root = aux
        elif node == node.parent.right:
            node.parent.right = aux
        else:
            node.parent.left = aux

        aux.right = node
        node.parent = aux

    def insert(self, key):
        self.adjustments.clear()

        novo = RBNode(key)
        novo.left = self.NIL
        novo.right = self.NIL

        pai = None
        atual = self.root

        while atual != self.NIL:
            pai = atual

            if novo.key < atual.key:
                atual = atual.left
            elif novo.key > atual.key:
                atual = atual.right
            else:
                return

        novo.parent = pai

        if pai is None:
            self.root = novo
        elif novo.key < pai.key:
            pai.left = novo
        else:
            pai.right = novo

        if novo.parent is None:
            novo.color = "BLACK"
            return

        self.fix_insert(novo)

    def fix_insert(self, node):
        while node.parent and node.parent.color == "RED":

            avo = node.parent.parent

            if node.parent == avo.right:
                tio = avo.left

                if tio.color == "RED":
                    self.adjustments.append("Recoloração dos nós")
                    tio.color = "BLACK"
                    node.parent.color = "BLACK"
                    avo.color = "RED"
                    node = avo

                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = "BLACK"
                    avo.color = "RED"
                    self.rotate_left(avo)

            else:
                tio = avo.right

                if tio.color == "RED":
                    self.adjustments.append("Recoloração dos nós")
                    tio.color = "BLACK"
                    node.parent.color = "BLACK"
                    avo.color = "RED"
                    node = avo

                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = "BLACK"
                    avo.color = "RED"
                    self.rotate_right(avo)

            if node == self.root:
                break

        self.root.color = "BLACK"

    def search(self, key):
        atual = self.root

        while atual != self.NIL:
            if key == atual.key:
                return atual
            elif key < atual.key:
                atual = atual.left
            else:
                atual = atual.right

        return None

    def transplant(self, antigo, novo):
        if antigo.parent is None:
            self.root = novo
        elif antigo == antigo.parent.left:
            antigo.parent.left = novo
        else:
            antigo.parent.right = novo

        novo.parent = antigo.parent

    def minimum(self, node):
        atual = node

        while atual.left != self.NIL:
            atual = atual.left

        return atual

    def delete(self, key):
        self.adjustments.clear()

        node = self.search(key)

        if node is None:
            return

        removido = node
        cor_original = removido.color

        if node.left == self.NIL:
            substituto = node.right
            self.transplant(node, node.right)

        elif node.right == self.NIL:
            substituto = node.left
            self.transplant(node, node.left)

        else:
            removido = self.minimum(node.right)
            cor_original = removido.color
            substituto = removido.right

            if removido.parent == node:
                substituto.parent = removido
            else:
                self.transplant(removido, removido.right)
                removido.right = node.right
                removido.right.parent = removido

            self.transplant(node, removido)
            removido.left = node.left
            removido.left.parent = removido
            removido.color = node.color

        if cor_original == "BLACK":
            self.fix_delete(substituto)

    def fix_delete(self, node):
        while node != self.root and node.color == "BLACK":

            if node == node.parent.left:
                irmao = node.parent.right

                if irmao.color == "RED":
                    self.adjustments.append("Recoloração dos nós")
                    irmao.color = "BLACK"
                    node.parent.color = "RED"
                    self.rotate_left(node.parent)
                    irmao = node.parent.right

                if irmao.left.color == "BLACK" and irmao.right.color == "BLACK":
                    self.adjustments.append("Recoloração dos nós")
                    irmao.color = "RED"
                    node = node.parent

                else:
                    if irmao.right.color == "BLACK":
                        self.adjustments.append("Recoloração dos nós")
                        irmao.left.color = "BLACK"
                        irmao.color = "RED"
                        self.rotate_right(irmao)
                        irmao = node.parent.right

                    irmao.color = node.parent.color
                    node.parent.color = "BLACK"
                    irmao.right.color = "BLACK"
                    self.rotate_left(node.parent)
                    node = self.root

            else:
                irmao = node.parent.left

                if irmao.color == "RED":
                    self.adjustments.append("Recoloração dos nós")
                    irmao.color = "BLACK"
                    node.parent.color = "RED"
                    self.rotate_right(node.parent)
                    irmao = node.parent.left

                if irmao.right.color == "BLACK" and irmao.left.color == "BLACK":
                    self.adjustments.append("Recoloração dos nós")
                    irmao.color = "RED"
                    node = node.parent

                else:
                    if irmao.left.color == "BLACK":
                        self.adjustments.append("Recoloração dos nós")
                        irmao.right.color = "BLACK"
                        irmao.color = "RED"
                        self.rotate_left(irmao)
                        irmao = node.parent.left

                    irmao.color = node.parent.color
                    node.parent.color = "BLACK"
                    irmao.left.color = "BLACK"
                    self.rotate_right(node.parent)
                    node = self.root

        node.color = "BLACK"

    def show_in_order(self):
        self._show_in_order(self.root)
        print()

    def _show_in_order(self, node):
        if node != self.NIL:
            self._show_in_order(node.left)
            print(f"{node.key}({node.color})", end=" ")
            self._show_in_order(node.right)

    def visualize(self):
        dot = Digraph()
        dot.attr('node', shape='circle')

        def add_nodes(node):
            if node == self.NIL:
                return

            if node.color == "RED":
                cor = "red"
            else:
                cor = "black"

            dot.node(
                str(node.key),
                style="filled",
                fillcolor=cor,
                fontcolor="white"
            )

            if node.left != self.NIL:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes(node.left)

            if node.right != self.NIL:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes(node.right)

        add_nodes(self.root)
        return dot
