from typing import List, Tuple


def solution(matrix: List[List[int]]) -> None:
    # Worst Case -> Time: O(m * n), Space: O(n)
    positions_with_0: List[Tuple[int, int]] = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                if (i, j) not in positions_with_0:
                    positions_with_0.append((i, j))

    for row, col in positions_with_0:
        matrix[row] = [0 for _ in range(len(matrix[row]))]
        for i in range(len(matrix)):
            matrix[i][col] = 0


if __name__ == '__main__':
    matrix = [[5, 1, 1], [1, 1, 1], [0, 2, 0]]
    solution(matrix)
    print(matrix)
