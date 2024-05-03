from typing import Any
from random import randint


class Node:
    def __init__(self, key: int, data: Any) -> None:
        self.key: int = key  # Identifier
        self.data: Any = data
        self.left: Node = None
        self.right: Node = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.__root: Node = None
        self.__count: int = 0

    def get_root(self) -> Node | None:
        if self.__root is None:
            return None

        return self.__root

    def __insert_help(self, root: Node, key: int, data: Any) -> Node:
        if root is None:
            return Node(key, data)

        if root.key > key:
            root.left = self.__insert_help(root.left, key, data)
        else:
            root.right = self.__insert_help(root.right, key, data)

        return root

    def insert(self, key: int, data: Any) -> None:
        self.__root = self.__insert_help(self.__root, key, data)
        self.__count += 1

    def __find_help(self, root: Node, key: int) -> Any | None:
        if root is None:
            return None

        if root.key > key:
            return self.__find_help(root.left, key)

        if root.key < key:
            return self.__find_help(root.right, key)

        return root.data

    def find(self, key: int) -> Any | None:
        return self.__find_help(self.__root, key)

    def __get_min(self, root: Node) -> Node:
        if root.left is None:
            return root

        return self.__get_min(root.left)

    def __delete_min(self, root: Node) -> Node:
        if root.left is None:
            return root.right

        root.left = self.__delete_min(root.left)

        return root

    def __remove_help(self, root: Node, key: int) -> Node | None:
        if root is None:
            return None

        if root.key > key:
            root.left = self.__remove_help(root.left, key)

        elif root.key < key:
            root.right = self.__remove_help(root.right, key)

        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self.__get_min(root.right)
            root.data, root.key = temp.data, temp.key
            root.right = self.__delete_min(root.right)

        return root

    def remove(self, key: int) -> Any:
        removed_data = self.__find_help(self.__root, key)
        if removed_data is not None:
            self.__root = self.__remove_help(self.__root, key)
            self.__count -= 1

        return removed_data


bst = BinarySearchTree()
for i in range(10):
    value = randint(10, 40)
    bst.insert(i, value)
    print(i, value)

print('-' * 10)

bst.remove(5)

for i in range(10):
    print(i, bst.find(i))
