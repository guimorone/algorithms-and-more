from random import randint
from typing import List, Any


def solution_1(matrix: List[List[Any]]) -> None:
    # Worst Case -> Time: O(n²), Space: O(n²)
    # Pode botar para dentro do primeiro for, deixando a complexidade espacial em O(n)
    temp = [[e for e in arr] for arr in matrix]
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            matrix[j][size - i - 1] = temp[i][j]


def solution_2(matrix: List[List[Any]]) -> None:
    # Worst Case -> Time: O(n²), Space: O(1)
    size = len(matrix)
    if not size:
        return

    for layer in range(size // 2):
        first = layer
        last = size - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    solution_2(matrix)
    print(matrix)
    for i in range(3):
        size = randint(3, 10)
        matrix = [[randint(1, 10) for _ in range(size)] for _ in range(size)]
        print('Result', f'{i}:')
        print('Before:', matrix)
        solution_1(matrix)
        print('After:', matrix)
