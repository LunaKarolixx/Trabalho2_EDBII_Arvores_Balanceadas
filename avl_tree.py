%%writefile avl_tree.py

from graphviz import Digraph


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.rotacoes = []

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def visualize(self, root):
        dot = Digraph()
        dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

        def add_nodes(node):
            if not node:
                return

            dot.node(str(node.key))

            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes(node.left)

            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes(node.right)

        add_nodes(root)
        return dot

    def rotate_right(self, y):
        self.rotacoes.append("Rotação simples à direita (LL)")

        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        self.rotacoes.append("Rotação simples à esquerda (RR)")

        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance_factor(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            self.rotacoes.append("Rotação dupla à direita (LR)")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            self.rotacoes.append("Rotação dupla à esquerda (RL)")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node

        while current.left:
            current = current.left

        return current

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance_factor(root)

        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.balance_factor(root.left) < 0:
            self.rotacoes.append("Rotação dupla à direita (LR)")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.balance_factor(root.right) > 0:
            self.rotacoes.append("Rotação dupla à esquerda (RL)")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, key):
        if not root:
            return None

        if root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
