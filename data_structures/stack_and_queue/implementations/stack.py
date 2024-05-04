from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node = None


class Stack:
    def __init__(self) -> None:
        self.top: Node = None
        self.__length: int = 0

    def is_empty(self) -> bool:
        return self.top is None

    def pop(self) -> Any:
        if self.is_empty():
            return None

        data, self.top = self.top.data, self.top.next
        self.__length -= 1

        return data

    def push(self, data: Any) -> None:
        new_node: Node = Node(data)
        new_node.next, self.top = self.top, new_node
        self.__length += 1

    def peek(self) -> Any:
        return self.top.data if not self.is_empty() else None

    def size(self) -> int:
        if self.is_empty():
            return 0

        length: int = 0
        current: Node = self.top
        while current:
            length += 1
            current = current.next

        return length

    def print_stack(self) -> None:
        if self.is_empty():
            print('Stack is empty')
            return

        current: Node = self.top
        while current:
            print(current.data, end=' -> ' if current.next is not None else '\n')
            current = current.next


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.print_stack()
    stack.pop()
    stack.push(3)
    stack.print_stack()
    stack.push(4)
    print(stack.peek())
    stack.print_stack()
