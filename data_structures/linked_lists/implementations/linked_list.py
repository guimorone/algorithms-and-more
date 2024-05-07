from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.__length: int = 0

    # Insert a new node at the beginning
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.__length += 1
            return
        else:
            new_node.next = self.head
            self.head = new_node

        self.__length += 1

    # Append a new node at the end
    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.__length += 1
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        self.__length += 1

    # Insert a new node in a certain index
    def insert_at_index(self, data: Any, index: int) -> None:
        if index < 0 or index > self.__length:
            raise IndexError('Index out of range')
        if index == 0:
            return self.insert(data)
        if index == self.__length:
            return self.append(data)

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError('Index out of range')
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.__length += 1

    def find(self, data: Any) -> int:
        if self.is_empty():
            return -1

        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index

            current = current.next
            index += 1

        return -1

    def count(self, data: Any) -> int:
        if self.is_empty():
            return -1

        current = self.head
        count = 0
        while current:
            if current.data == data:
                count += 1

            current = current.next

        return count

    def update_node(self, data: Any, index: int) -> None:
        if index < 0 or index >= self.__length:
            raise IndexError('Index out of range')

        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError('Index out of range')
            current = current.next

        current.data = data

    def remove_first(self) -> None:
        if self.head is None:
            return

        self.head = self.head.next
        self.__length -= 1

    def remove_last(self) -> None:
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            self.__length -= 1
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None
        self.__length -= 1

    def remove_at_index(self, index: int) -> None:
        if index < 0 or index >= self.__length:
            raise IndexError('Index out of range')

        if index == 0:
            return self.remove_first()
        if index == self.__length - 1:
            return self.remove_last()

        current = self.head
        for _ in range(index - 1):
            current = current.next
            if current is None:
                raise IndexError('Index out of range')

        current.next = current.next.next
        self.__length -= 1

    def remove(self, data: Any) -> None:
        if self.is_empty():
            return

        current = self.head
        if current.data == data:
            self.head = self.head.next
            return

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

    def clear(self) -> None:
        self.head = None
        self.__length = 0

    def size(self) -> int:
        length = 0
        if self.head is not None:
            current = self.head
            while current:
                length += 1
                current = current.next

            return length
        else:
            return 0

    def length(self) -> int:
        return self.__length

    def is_empty(self) -> bool:
        return self.__length == 0 or self.head is None

    def print_list(self, title: Optional[str] = None) -> None:
        if title:
            print(title)
        current = self.head
        if current is None:
            print('EMPTY', end='')
            return
        while current:
            print(current.data, end=' -> ' if current.next else '\n')
            current = current.next
