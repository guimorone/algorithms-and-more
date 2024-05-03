from typing import List


def is_pair_sum(array: List[int], value: int) -> bool:
    first_pointer = 0
    second_pointer = len(array) - 1

    while first_pointer < second_pointer:
        if array[first_pointer] + array[second_pointer] == value:
            print(f'Pair found: {array[first_pointer]} + {array[second_pointer]} = {value}')
            return True

        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i++
        elif array[first_pointer] + array[second_pointer] < value:
            first_pointer += 1

        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j--
        else:
            second_pointer -= 1

    print('Pair not found')
    return False


arr = [2, 3, 5, 8, 9, 10, 11]
arr.sort()
val = 18
print(is_pair_sum(arr, val))
