from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node = None


class Queue:
    def __init__(self) -> None:
        self.first: Node = None
        self.__length: int = 0

    def is_empty(self) -> bool:
        return self.first is None

    def remove(self) -> Any:
        if self.is_empty():
            return None

        data, self.first = self.first.data, self.first.next
        self.__length -= 1

        return data

    # Para otimizar -> adicionar o nó "last" para evitar percorrer a fila inteira
    def add(self, data: Any) -> None:
        new_node: Node = Node(data)
        if self.is_empty():
            self.first = new_node
        else:
            current: Node = self.first
            while current.next:
                current = current.next
            current.next = new_node

        self.__length += 1

    def peek(self) -> Any:
        return self.first.data if not self.is_empty() else None

    def size(self) -> int:
        if self.is_empty():
            return 0

        length: int = 0
        current: Node = self.first
        while current:
            length += 1
            current = current.next

        return length

    def print_queue(self) -> None:
        if self.is_empty():
            print('Queue is empty')
            return

        current: Node = self.first
        while current:
            print(current.data, end=' <- ' if current.next is not None else '\n')
            current = current.next


if __name__ == '__main__':
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.print_queue()
    queue.remove()
    queue.add(3)
    queue.print_queue()
    queue.add(4)
    print(queue.peek())
    queue.print_queue()
