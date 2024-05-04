from abc import ABC, abstractmethod
from typing import List, Tuple, Literal


class Graph(ABC):
    def __init__(
        self,
        adjacencies: List[List[Tuple[int, int] | int]],
        adjacency_type: Literal['list', 'matrix'],
    ) -> None:
        # Tuple -> Vertex and Weight
        # Weight must be greater than 0
        self.adjacencies: List[List[Tuple[int, int] | int]] = adjacencies
        self._adjacency_type: Literal['list', 'matrix'] = adjacency_type
        self.sort_adjacencies_array()
        self._mark: List[bool] = [False] * len(self.adjacencies)

    def sort_adjacencies_array(self) -> None:
        if self._adjacency_type != 'list':
            return

        self.adjacencies: List[List[Tuple[int, int]]] = [sorted(l, key=lambda t: t[0]) for l in self.adjacencies]

    def search_in_list(self, i: int, j: int) -> Tuple[int, int]:
        if self._adjacency_type != 'list':
            raise ValueError('This method is only for adjacency list graphs.')

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

        if self._adjacency_type == 'list':
            if not self.adjacencies[vertex] or not len(self.adjacencies[vertex]):
                return -1

            return self.adjacencies[vertex][0][0]

        for i in range(len(self.adjacencies[vertex])):
            if self.adjacencies[vertex][i] > 0:
                return i

        return -1

    def next(self, vertex: int, reference_vertex: int) -> int:
        # first vertex AFTER 'reference_vertex'
        # considering adjacencies sorted
        # -1 = absence
        if vertex >= len(self.adjacencies) or reference_vertex >= len(self.adjacencies):
            return -1

        if self._adjacency_type == 'list':
            for v, _ in self.adjacencies[vertex]:
                if v <= reference_vertex:
                    continue

                return v

        else:
            for i in range(reference_vertex + 1, len(self.adjacencies[vertex])):
                if self.adjacencies[vertex][i] > 0:
                    return i

        return -1

    def set_edge(self, i: int, j: int, w: int = 1) -> None:
        if w <= 0:
            raise ValueError('Weight must be greater than 0')

        if self._adjacency_type == 'list':
            index_i, index_j = self.search_in_list(i, j)
            if index_i == -1 and index_j == -1:
                self.adjacencies[i].append((j, w))
                self.adjacencies[j].append((i, w))
                self.sort_adjacencies_array()
            elif index_i == -1 or index_j == -1:
                raise ValueError('This graph is bidirectional, you must provide both edges.')
        else:
            self.adjacencies[i][j] = w
            self.adjacencies[j][i] = w

    def del_edge(self, i: int, j: int) -> None:
        if self._adjacency_type == 'list':
            index_i, index_j = self.search_in_list(i, j)
            if index_i != -1:
                del self.adjacencies[i][index_i]
            if index_j != -1:
                del self.adjacencies[j][index_j]
        else:
            self.adjacencies[i][j] = -1
            self.adjacencies[j][i] = -1

    def graph_traverse(self, *args, **kwargs) -> None:
        # To ensure all nodes are visited (unconnected graphs problem)
        for i in range(len(self.adjacencies)):
            if self._mark[i] is False:
                self._traverse(i, *args, **kwargs)

    def get_marks(self) -> List[bool]:
        return self._mark

    @abstractmethod
    def _traverse(self, vertex: int, *args, **kwargs) -> None: ...


if __name__ == '__main__':
    # REMOVE ABC FROM GRAPH BEFORE TESTING
    adjacencies_list = [[(2, 1)], [(2, 3)], [(1, 3), (0, 1)]]
    adjacencies_matrix = [[-1, 1, -1], [1, -1, 3], [-1, 3, -1]]
    graph_list = Graph(adjacencies_list, 'list')
    print(graph_list.adjacencies)
    graph_list.set_edge(0, 1, 4)
    print(graph_list.adjacencies)
    graph_list.del_edge(0, 1)
    print(graph_list.adjacencies)

    graph_matrix = Graph(adjacencies_matrix, 'matrix')
    print(graph_matrix.adjacencies)
    graph_matrix.set_edge(0, 1, 4)
    print(graph_matrix.adjacencies)
    graph_matrix.del_edge(0, 1)
    print(graph_matrix.adjacencies)
