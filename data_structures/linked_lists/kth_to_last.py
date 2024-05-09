from typing import Any
from implementations.linked_list import LinkedList


def solution_1(linked_list: LinkedList, k: int) -> Any:
    # Worst Case -> Time: O(n), Space: O(n)
    # If we do NOT know the 'linked_list' size
    # k == 0 -> return the last element
    items = []
    current = linked_list.head
    while current:
        items.append(current.data)
        current = current.next

    return items[len(items) - k - 1] if k < len(items) else None


def solution_2(linked_list: LinkedList, k: int) -> Any:
    # Worst Case -> Time: O(n), Space: O(1)
    # If we know the 'linked_list' size
    # k == 0 -> return the last element
    current = linked_list.head
    index = -1
    target_index = linked_list.length() - k - 1
    while current:
        index += 1
        if index == target_index:
            return current.data
        current = current.next

    return None


def solution_3(linked_list: LinkedList, k: int) -> Any:
    # Worst Case -> Time: O(n), Space: O(1)
    # If we do NOT know the 'linked_list' size
    # k == 1 -> return the last element, in order to k == 0 return the last element, change the for loop range to 'k + 1' instead of 'k'
    p1 = linked_list.head
    p2 = linked_list.head
    for _ in range(k):
        if p2 is None:
            # Out of bounds
            return None
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next

    return p1.data if p1 else None


if __name__ == '__main__':
    l = [i for i in range(10)]
    linked_list = LinkedList()
    for e in l:
        linked_list.append(e)
    linked_list.print_list()
    print(solution_1(linked_list, 4))
    print(solution_2(linked_list, 4))
    print(solution_3(linked_list, 4))
