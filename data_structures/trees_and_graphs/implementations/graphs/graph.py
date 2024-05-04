from typing import List, Tuple


class Graph:
    def __init__(self, adjacencies: List[List[Tuple[int, int]]]) -> None:
        # Tuple -> Vertex and Weight
        # Weight must be greater than 0
        self.adjacencies: List[List[Tuple[int, int]]] = adjacencies
        self.sort_adjacencies_array()

    def sort_adjacencies_array(self) -> None:
        self.adjacencies = [sorted(l, key=lambda t: t[0]) for l in self.adjacencies]

    def search(self, i: int, j: int) -> Tuple[int, int]:
        index_i = -1
        index_j = -1
        for n in range(len(self.adjacencies[i])):
            if self.adjacencies[i][n][0] == j:
                index_i = n
                break

        for n in range(len(self.adjacencies[j])):
            if self.adjacencies[j][n][0] == i:
                index_j = n
                break

        return index_i, index_j

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

    def set_edge(self, i: int, j: int, w: int = 1) -> None:
        if w <= 0:
            raise ValueError('Weight must be greater than 0')

        index_i, index_j = self.search(i, j)
        if index_i == -1 and index_j == -1:
            self.adjacencies[i].append((j, w))
            self.adjacencies[j].append((i, w))
            self.sort_adjacencies_array()
        elif index_i == -1 or index_j == -1:
            raise ValueError('This graph is bidirectional, you must provide both edges.')

    def del_edge(self, i: int, j: int) -> None:
        index_i, index_j = self.search(i, j)
        if index_i != -1:
            del self.adjacencies[i][index_i]
        if index_j != -1:
            del self.adjacencies[j][index_j]


if __name__ == '__main__':
    adjacencies = [[(2, 1)], [(2, 3)], [(1, 3), (0, 1)]]
    graph = Graph(adjacencies)
    print(graph.adjacencies)
    graph.set_edge(0, 1, 4)
    print(graph.adjacencies)
    graph.del_edge(0, 1)
    print(graph.adjacencies)
