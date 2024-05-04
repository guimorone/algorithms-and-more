from typing import Literal
from graph import Graph
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'stack_and_queue', 'implementations'))
from stack import Stack


class DFS(Graph):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__stack: Stack = Stack()

    def _traverse(self, vertex: int, traverse_type: Literal['dfs', 'toposort'] = 'dfs') -> None:
        if traverse_type == 'dfs':
            self.do_dfs(vertex)
        elif traverse_type == 'toposort':
            self.toposort(vertex)

    def do_dfs(self, vertex: int) -> None:
        if vertex >= len(self.adjacencies):
            return

        self._visited_list[vertex] = True
        j = self.first(vertex)
        while j != -1 and j < len(self.adjacencies):
            if j == -1:
                # absence
                break

            if self._visited_list[j] is False:
                self.do_dfs(j)

            j = self.next(vertex, j)

    def toposort(self, vertex: int) -> None:
        if vertex >= len(self.adjacencies):
            return

        self._visited_list[vertex] = True
        j = self.first(vertex)
        while j != -1 and j < len(self.adjacencies):
            if self._visited_list[j] is False:
                self.toposort(j)

            j = self.next(vertex, j)

        self.__stack.push(vertex)

    def print_stack(self) -> None:
        self.__stack.print_stack()


if __name__ == '__main__':
    adjacencies_list = [[(2, 1)], [(2, 3)], [(1, 3), (0, 1)]]
    adjacencies_matrix = [[-1, 1, 1], [1, -1, 3], [1, 3, -1]]
    dfs_list = DFS(adjacencies_list, 'list')
    dfs_matrix = DFS(adjacencies_matrix, 'matrix')
    print(dfs_list.get_visited_lists())
    print(dfs_matrix.get_visited_lists())
    dfs_list.graph_traverse()
    dfs_matrix.graph_traverse()
    print(dfs_list.get_visited_lists())
    print(dfs_matrix.get_visited_lists())

    toposort_matrix = [
        [-1, 1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 1, 1, 1, -1],
        [-1, -1, -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, 1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
    ]

    t = DFS(toposort_matrix, 'matrix')
    t.graph_traverse('toposort')
    t.print_stack()
