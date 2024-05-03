from typing import List, Literal


class Heap:
    def __init__(
        self,
        heap_type: Literal['min', 'max'] = 'min',
        heap_method: Literal['bottom-up', 'top-down'] = 'bottom-up',
        nodes: List[int] = [],
    ) -> None:
        self.nodes: List[int] = nodes
        self.heap_type: Literal['min', 'max'] = heap_type
        self.heap_method: Literal['bottom-up', 'top-down'] = heap_method
        self.__heap: List[int] = [float('inf') if self.heap_type == 'max' else -1]
        self.__size: int = 0

    def position_heapify(self, pos: int) -> None:
        value = self.__heap[pos]
        heap = False
        while not heap and 2 * pos <= self.__size:
            j = 2 * pos
            if j < self.__size:
                if (
                    self.heap_type == 'max'
                    and self.__heap[j] < self.__heap[j + 1]
                    or self.heap_type == 'min'
                    and self.__heap[j] > self.__heap[j + 1]
                ):
                    j += 1

            if (
                self.heap_type == 'max'
                and value >= self.__heap[j]
                or self.heap_type == 'min'
                and value <= self.__heap[j]
            ):
                heap = True
            else:
                self.__heap[pos] = self.__heap[j]
                pos = j

        self.__heap[pos] = value

    def insert(self, element: int) -> None:
        self.__heap.append(element)
        self.__size += 1

        current = self.__size
        parent = current // 2
        while (
            self.heap_type == 'max'
            and self.__heap[current] > self.__heap[parent]
            or self.heap_type == 'min'
            and self.__heap[current] < self.__heap[parent]
        ):
            self.__heap[current], self.__heap[parent] = self.__heap[parent], self.__heap[current]
            current = parent
            parent = current // 2

    def pop(self) -> int:
        popped = self.__heap[1]
        self.__heap[1] = self.__heap[self.__size]
        self.__size -= 1
        self.position_heapify(1)

        return popped

    def __bottom_up(self) -> None:
        for pos in range(self.__size // 2, 0, -1):
            self.position_heapify(pos)

    def __top_down(self) -> None:
        for element in self.nodes:
            self.insert(element)

    def heapify(self) -> None:
        if self.heap_method == 'bottom-up':
            self.__heap: List[int] = [-1] + self.nodes
            self.__size: int = len(self.nodes)
            self.__bottom_up()
        elif self.heap_method == 'top-down':
            self.__heap: List[int] = [float('inf') if self.heap_type == 'max' else -1]
            self.__size: int = 0
            self.__top_down()
        else:
            raise ValueError('Method not recognized')

    def get_heap(self) -> List[int]:
        return self.__heap[1:]

    def get_peek_value(self) -> int:
        return self.__heap[1]


if __name__ == '__main__':
    array = [5, 3, 17, 9, 84, 19, 6, 22, 10]
    array_2 = [2, 9, 7, 6, 5, 8, 10]
    heap_1 = Heap(heap_method='bottom-up', nodes=array)
    heap_2 = Heap(heap_type='max', nodes=array)
    heap_3 = Heap(nodes=array_2)
    heap_4 = Heap('max', 'top-down', array_2)
    heap_5 = Heap(heap_method='top-down')
    for i in range(7):
        heap_5.insert(7 - i + 1)

    heap_1.heapify()
    heap_2.heapify()
    heap_3.heapify()
    heap_4.heapify()
    print(heap_1.get_heap())
    print(heap_2.get_heap())
    print(heap_3.get_heap())
    print(heap_4.get_heap())
    print(heap_5.get_heap())
    print(heap_1.pop())
    print(heap_1.pop())
    print(heap_1.pop())
    print(heap_1.pop())
    print(heap_2.pop())
    print(heap_2.pop())
    print(heap_2.pop())
