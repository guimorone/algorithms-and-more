from random import randint, choice
from typing import Literal, List, Any, Optional


def quicksort(
    array: List[Any],
    sort_type: Literal['asc', 'desc'] = 'asc',
    left_index: Optional[int] = None,
    right_index: Optional[int] = None,
) -> None:
    def partition(l: int, r: int) -> int:
        p = array[l]
        i = l
        j = r + 1
        while i < j:
            i += 1
            j -= 1
            while ((sort_type == 'asc' and array[i] < p) or (sort_type == 'desc' and array[i] > p)) and i < r:
                i += 1
            while ((sort_type == 'asc' and array[j] > p) or (sort_type == 'desc' and array[j] < p)) and j > 0:
                j -= 1
            array[i], array[j] = array[j], array[i]
        # undo last swap
        array[i], array[j] = array[j], array[i]
        array[l], array[j] = array[j], array[l]
        return j

    if left_index is None:
        left_index = 0
    if right_index is None:
        right_index = len(array) - 1

    if left_index >= len(array) or right_index >= len(array):
        return

    if left_index < right_index:
        partition_index = partition(left_index, right_index)
        quicksort(array, sort_type, left_index, partition_index - 1)
        quicksort(array, sort_type, partition_index + 1, right_index)


if __name__ == '__main__':
    for i in range(10):
        print('Result', f'{i + 1}:')
        array = [randint(0, 15) for _ in range(10)]
        sort_type = choice(['asc', 'desc'])
        print('Before:', array)
        quicksort(array, sort_type)
        print('After:', array)
        print(sort_type)
