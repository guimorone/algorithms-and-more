# Fazendo isso para não precisar reescrever a linked_list aqui
import sys, os
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'linked_lists', 'implementations'))
from linked_list import LinkedList


class HashTable:
    def __init__(self, length: int = 5) -> None:
        self.__length = length
        self.__addresses: List[LinkedList] = [LinkedList() for _ in range(length)]

    def hash_function(self, key: object) -> int:
        return ord(key) % self.__length

    def insert(self, key: object) -> None:
        hash_key = self.hash_function(key)
        self.__addresses[hash_key].append(key)

    def search(self, key: object) -> bool:
        hash_key = self.hash_function(key)
        index = self.__addresses[hash_key].find(key)

        return index != -1
    
    def count(self, key: object) -> int:
        hash_key = self.hash_function(key)
        count = self.__addresses[hash_key].count(key)

        return count

    def delete(self, key: object) -> None:
        hash_key = self.hash_function(key)
        self.__addresses[hash_key].remove(key)

    def print_hash_table(self) -> None:
        for i in range(self.__length):
            print(f'[{i}]:', end=' ')
            self.__addresses[i].print_list()
            print()


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.insert('aaaa')
    hash_table.insert('bbbb')
    hash_table.insert('ccc')
    print(hash_table.search('aaaa'))
    hash_table.print_hash_table()
    hash_table.delete('bbbb')
    print(hash_table.search('bbbb'))
    hash_table.insert('ddd')
    hash_table.print_hash_table()
