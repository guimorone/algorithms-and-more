from typing import List, Tuple


class Graph:
    def __init__(self, adjacencies: List[List[Tuple[int, int]]]) -> None:
        # Tuple -> Vertex and Weight
        # Weight must be greater than 0
        self.adjacencies: List[List[Tuple[int, int]]] = [sorted(l, key=lambda t: t[0]) for l in adjacencies]
        print(self.adjacencies)
        self.__marks: List[int] = []
        self.__num_edge = 0

    def first(self, vertex: int) -> int:
        # -1 = absence
        if vertex >= len(self.adjacencies):
            return -1

        if not self.adjacencies[vertex] or not len(self.adjacencies[vertex]):
            return -1

        return self.adjacencies[vertex][0][0]

    def next(self, vertex: int, reference_vertex: int) -> int:
        # first vertex AFTER 'reference_vertex'
        # considering adjacencies sorted
        # -1 = absence
        if vertex >= len(self.adjacencies):
            return -1

        for v, _ in self.adjacencies[vertex]:
            if v <= reference_vertex:
                continue
            
            return v

        return -1


if __name__ == '__main__':
    adjacencies = [[(2, 1)], [(2, 3)], [(1, 3), (0, 1)]]
    graph = Graph(adjacencies)
    print(graph.first(0))
