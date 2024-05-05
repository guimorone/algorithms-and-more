import math
from typing import List
from graph import Graph


def floyd_warshall(graph: Graph) -> List[List[int]]:
    size = len(graph.adjacencies)
    distances = [[graph.get_weight(i, j) if i != j else 0 for j in range(size)] for i in range(size)]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if (
                    distances[i][k] != math.inf
                    and distances[k][j] != math.inf
                    and distances[i][j] > distances[i][k] + distances[k][j]
                ):
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances


if __name__ == '__main__':
    adjacencies = [
        [math.inf, math.inf, 3, math.inf],
        [2, math.inf, math.inf, math.inf],
        [math.inf, 7, math.inf, 1],
        [6, math.inf, math.inf, math.inf],
    ]
    graph = Graph(adjacencies, 'matrix')
    distances = floyd_warshall(graph)
    for i in range(len(distances)):
        print(f'Origem {i}:', end=' ')
        for j in range(len(distances[i])):
            print(distances[i][j], end=' ')
        print()
