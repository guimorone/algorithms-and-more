from typing import Any
from implementations.linked_list import LinkedList


def solution_1(linked_list: LinkedList, value: Any) -> LinkedList:
    # Worst Case -> Time: O(n²) due to append operator, Space: O(n)
    new_linked_list = LinkedList()
    current = linked_list.head
    while current:
        if current.data < value:
            new_linked_list.insert(current.data)
        else:
            new_linked_list.append(current.data)
        current = current.next

    return new_linked_list

def solution_2(linked_list: LinkedList, value: Any) -> LinkedList:
    # Worst Case -> Time: O(n), Space: O(n)
    linked_list_before = LinkedList()
    linked_list_after = LinkedList()
    current = linked_list.head
    while current:
        if current.data < value:
            linked_list_before.insert(current.data)
        else:
            linked_list_after.insert(current.data)
        current = current.next
        
    last = linked_list_before.head
    while last.next:
        last = last.next
        
    last.next = linked_list_after.head

    return linked_list_before

if __name__ == '__main__':
    l = [3, 5, 8, 5, 10, 2, 1]
    linked_list = LinkedList()
    for e in l:
        linked_list.append(e)
    linked_list.print_list('Before')
    solution_1(linked_list, 5).print_list('After 1')
    solution_2(linked_list, 5).print_list('After 2')
