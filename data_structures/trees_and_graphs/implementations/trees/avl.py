from typing import Any
from random import randint
from bst import Node, BinarySearchTree


class AVLNode(Node):
    def __init__(self, key: int, data: Any) -> None:
        self.height: int = 0
        super().__init__(key, data)


class AVL(BinarySearchTree):
    def get_height(self, root: AVLNode) -> int:
        if root is None:
            return -1

        return root.height

    def get_balance(self, root: AVLNode) -> int:
        if root is None:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, root: AVLNode) -> AVLNode:
        l = root.left  # new left node
        lr = l.right  # right node OF THE new left node
        l.right = root
        root.left = lr

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        l.height = 1 + max(self.get_height(l.left), self.get_height(l.right))

        return l

    def left_rotate(self, root: AVLNode) -> AVLNode:
        r = root.right  # new right node
        rl = r.left  # left node OF THE new right node
        r.left = root
        root.right = rl

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        r.height = 1 + max(self.get_height(r.left), self.get_height(r.right))

        return r

    def _insert_help(self, root: AVLNode, key: int, data: Any) -> AVLNode:
        if root is None:
            return AVLNode(key, data)

        if root.key > key:
            root.left = self._insert_help(root.left, key, data)
        else:
            root.right = self._insert_help(root.right, key, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        if balance < -1 and key >= root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance > 1 and key >= root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


if __name__ == '__main__':
    bst = BinarySearchTree()
    avl = AVL()
    for i in range(10):
        value = randint(10, 40)
        bst.insert(i, value)
        avl.insert(i, value)

    # Comparing
    bst.print_tree()
    print('-' * 30, end='\n\n')
    avl.print_tree()
