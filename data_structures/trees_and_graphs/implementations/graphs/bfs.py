from graph import Graph
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'stack_and_queue', 'implementations'))
from custom_queue import Queue


class BFS(Graph):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _traverse(self, start_vertex: int) -> None:
        if start_vertex >= len(self.adjacencies):
            return

        queue = Queue()

        queue.add(start_vertex)
        self._visited_list[start_vertex] = True
        while not queue.is_empty():
            vertex = queue.remove()
            j = self.first(vertex)
            while j != -1:
                if self._visited_list[j] is False:
                    self._visited_list[j] = True
                    queue.add(j)

                j = self.next(vertex, j)


if __name__ == '__main__':
    adjacencies_list = [[(2, 1)], [(2, 3)], [(1, 3), (0, 1)]]
    adjacencies_matrix = [[-1, 1, 1], [1, -1, 3], [1, 3, -1]]
    bfs_list = BFS(adjacencies_list, 'list')
    bfs_matrix = BFS(adjacencies_matrix, 'matrix')
    print(bfs_list.get_visited_lists())
    print(bfs_matrix.get_visited_lists())
    bfs_list.graph_traverse()
    bfs_matrix.graph_traverse()
    print(bfs_list.get_visited_lists())
    print(bfs_matrix.get_visited_lists())
