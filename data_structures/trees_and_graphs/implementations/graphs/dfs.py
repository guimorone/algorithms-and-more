import math
import sys, os
from typing import Literal
from graph import Graph


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
        if vertex >= len(self.adjacencies) or vertex == -1:
            return

        self.visited_list[vertex] = True
        j = self.first(vertex)
        while j != -1:
            if self.visited_list[j] is False:
                self.do_dfs(j)

            j = self.next(vertex, j)

    def toposort(self, vertex: int) -> None:
        if vertex >= len(self.adjacencies) or vertex == -1:
            return

        self.visited_list[vertex] = True
        j = self.first(vertex)
        while j != -1:
            if self.visited_list[j] is False:
                self.toposort(j)

            j = self.next(vertex, j)

        self.__stack.push(vertex)

    def print_stack(self) -> None:
        self.__stack.print_stack()


if __name__ == '__main__':
    adjacencies_list = [[(2, 1)], [(2, 3)], [(1, 3), (0, 1)]]
    adjacencies_matrix = [[math.inf, 1, 1], [1, math.inf, 3], [1, 3, math.inf]]
    dfs_list = DFS(adjacencies_list, 'list')
    dfs_matrix = DFS(adjacencies_matrix, 'matrix')
    print(dfs_list.get_visited_lists())
    print(dfs_matrix.get_visited_lists())
    dfs_list.graph_traverse()
    dfs_matrix.graph_traverse()
    print(dfs_list.get_visited_lists())
    print(dfs_matrix.get_visited_lists())

    toposort_matrix = [
        [math.inf, 1, 1, math.inf, math.inf, math.inf, math.inf],
        [math.inf, math.inf, math.inf, 1, 1, 1, math.inf],
        [math.inf, math.inf, math.inf, 1, math.inf, math.inf, math.inf],
        [math.inf, math.inf, math.inf, math.inf, 1, math.inf, math.inf],
        [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 1],
        [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
        [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
    ]

    t = DFS(toposort_matrix, 'matrix')
    t.graph_traverse('toposort')
    t.print_stack()
