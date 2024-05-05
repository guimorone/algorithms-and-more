import math

import sys, os
from typing import List
from graph import Graph

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'trees'))
from heap import Heap
# import heapq


def dijkstra(graph: Graph, source_vertex: int) -> List[int]:
    size = len(graph.adjacencies)
    graph.visited_list = [False for _ in range(size)]
    distances = [math.inf for _ in range(size)]
    h = [(source_vertex, source_vertex, 0)]
    heap = Heap('min', 'top-down', h)
    heap.heapify()
    # heapq.heapify(h)
    distances[source_vertex] = 0
    for _ in range(size):
        try:
            # peek = heapq.heappop(h)
            peek = heap.pop()
            if peek is None:
                return distances
            _, v, _ = peek
            while graph.visited_list[v] is True:
                # peek = heapq.heappop(h)
                peek = heap.pop()
                if peek is None:
                    return distances
                _, v, _ = peek
        except:
            return distances

        graph.visited_list[v] = True
        w = graph.first(v)
        while w != -1:
            if graph.visited_list[w] is False and distances[w] > distances[v] + graph.get_weight(v, w):
                distances[w] = distances[v] + graph.get_weight(v, w)
                # heapq.heappush(h, (v, w, distances[w]))
                heap.push((v, w, distances[w]))

            w = graph.next(v, w)

    return distances


if __name__ == '__main__':
    adjacencies = [
        [math.inf, 10, 3, 20, math.inf],
        [math.inf, math.inf, math.inf, 5, math.inf],
        [math.inf, 2, math.inf, math.inf, 15],
        [math.inf, math.inf, math.inf, math.inf, 11],
        [math.inf, math.inf, math.inf, math.inf, math.inf],
    ]
    graph = Graph(adjacencies, 'matrix')
    for i in range(5):
        print(dijkstra(graph, i))
