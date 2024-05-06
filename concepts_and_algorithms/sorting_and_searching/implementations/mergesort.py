from random import randint, choice
from typing import Literal, List, Any, Optional


def mergesort(
    array: List[Any],
    sort_type: Literal['asc', 'desc'] = 'asc',
    left_index: Optional[int] = None,
    right_index: Optional[int] = None,
) -> None:
    def merge(l: int, r: int) -> None:
        temp = array.copy()
        m = (l + r) // 2
        i_1 = l
        i_2 = m + 1
        for i in range(l, r + 1):
            # já foi copiado tudo da esquerda
            if i_1 == m + 1:
                array[i] = temp[i_2]
                i_2 += 1
            # já foi copiado tudo da direita
            elif i_2 > r:
                array[i] = temp[i_1]
                i_1 += 1
            elif (sort_type == 'asc' and temp[i_1] <= temp[i_2]) or (
                sort_type == 'desc' and temp[i_1] >= temp[i_2]
            ):
                array[i] = temp[i_1]
                i_1 += 1
            else:
                array[i] = temp[i_2]
                i_2 += 1

    if left_index is None:
        left_index = 0
    if right_index is None:
        right_index = len(array) - 1

    if left_index >= len(array) or right_index >= len(array):
        return

    if left_index < right_index:
        middle_index = (left_index + right_index) // 2
        mergesort(array, sort_type, left_index, middle_index)
        mergesort(array, sort_type, middle_index + 1, right_index)
        merge(left_index, right_index)


if __name__ == '__main__':
    for i in range(10):
        print('Result', f'{i + 1}:')
        array = [randint(0, 15) for _ in range(10)]
        sort_type = choice(['asc', 'desc'])
        print('Before:', array)
        mergesort(array, sort_type)
        print('After:', array)
        print(sort_type)
