from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node = None


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
            if current is None:
                raise IndexError('Index out of range')
            current = current.next

        current.next = current.next.next
        self.__length -= 1

    def clear(self) -> None:
        self.head = None
        self.__length = 0

    def size(self) -> int:
        size = 0
        if self.head is not None:
            current = self.head
            while current:
                size += 1
                current = current.next

            return size
        else:
            return 0

    def length(self) -> int:
        return self.__length

    def is_empty(self) -> bool:
        return self.__length == 0

    def print_list(self, title: Optional[str]) -> None:
        if title:
            print(title)
        current = self.head
        while current:
            print(current.data)
            current = current.next
