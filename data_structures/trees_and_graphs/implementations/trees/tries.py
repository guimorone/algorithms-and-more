from typing import Dict, List
from collections import defaultdict


class Node:
    def __init__(self) -> None:
        # 1: If using '{}' instead of 'defaultdict', add the second comment in line 22
        self.children: Dict[str, Node] = defaultdict(Node)
        self.is_complete_word: bool = False


class Trie:
    def __init__(self, words: List[str] = []) -> None:
        self.root: Node = Node()
        if words and len(words):
            for word in words:
                self.insert(word)

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            # 2: Add this
            # new_node = Node()
            # current.children[letter] = new_node
            current = current.children[letter]
        current.is_complete_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False

        return current.is_complete_word

    def starts_with(self, prefix: str) -> bool:
        # If any starts with "prefix"
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False

        return True


if __name__ == '__main__':
    words = ['aaa', 'bbb']
    trie = Trie(words)
    result = trie.search('aaa')
    print(result)
    result = trie.starts_with('c')
    print(result)
