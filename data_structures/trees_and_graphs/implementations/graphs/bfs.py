from graph import Graph
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'stack_and_queue', 'implementations'))
from custom_queue import Queue


class BFS(Graph):
    def _traverse(self, start_vertex: int, destiny_vertex: int = -1) -> None:
        if start_vertex >= len(self.adjacencies) or start_vertex == -1:
            return
        if start_vertex == destiny_vertex:
            return

        predecessors = [start_vertex]
        queue = Queue()

        queue.add(start_vertex)
        self._visited_list[start_vertex] = True
        while not queue.is_empty():
            vertex = queue.remove()
            next_vertex = self.first(vertex)
            while next_vertex != -1:
                if self._visited_list[next_vertex] is False:
                    self._visited_list[next_vertex] = True
                    queue.add(next_vertex)
                    if destiny_vertex != -1:
                        predecessors.append(next_vertex)

                if destiny_vertex != -1 and next_vertex == destiny_vertex:
                    # considering unweighted graph
                    print('Found path!')
                    for i in range(len(predecessors)):
                        print(predecessors[i], end=' -> ' if i != len(predecessors) - 1 else '\n')

                    return

                next_vertex = self.next(vertex, next_vertex)


if __name__ == '__main__':
    adjacencies_list = [[(2, 1)], [(2, 3)], [(1, 3), (0, 1)]]
    adjacencies_matrix = [[-1, 1, 1], [1, -1, 3], [1, 3, -1]]
    bfs_list = BFS(adjacencies_list, 'list')
    bfs_matrix = BFS(adjacencies_matrix, 'matrix')
    print(bfs_list.get_visited_lists())
    print(bfs_matrix.get_visited_lists())
    bfs_list.graph_traverse()
    bfs_matrix.graph_traverse(destiny_vertex=2)
    print(bfs_list.get_visited_lists())
    print(bfs_matrix.get_visited_lists())
