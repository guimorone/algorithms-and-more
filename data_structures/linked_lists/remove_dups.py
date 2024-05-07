from random import randint
from implementations.linked_list import LinkedList


def solution_1(linked_list: LinkedList) -> None:
    # Worst Case -> Time: O(n²) (Iterate through each and then remove), Space: O(n)
    duplicates = []
    indexes_to_remove = []
    current = linked_list.head
    index = 0
    while current:
        if current.data in duplicates:
            indexes_to_remove.append(index)
        else:
            duplicates.append(current.data)
        current = current.next
        index += 1

    for i in range(len(indexes_to_remove)):
        linked_list.remove_at_index(indexes_to_remove[i] - i)


def solution_2(linked_list: LinkedList) -> None:
    # Worst Case -> Time: O(n), Space: O(n)
    # the head will never be duplicated
    current = linked_list.head
    if current is None:
        return
    duplicates = [current.data]
    while current.next:
        if current.next.data in duplicates:
            current.next = current.next.next
        else:
            duplicates.append(current.next.data)
            current = current.next

        if current is None:
            break


def solution_3(linked_list: LinkedList) -> None:
    # Worst Case -> Time: O(n²), Space: O(1)
    current = linked_list.head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


if __name__ == '__main__':
    l = [randint(1, 5) for _ in range(10)]
    linked_list_1 = LinkedList()
    for e in l:
        linked_list_1.append(e)
    linked_list_1.print_list('Before 1')
    solution_1(linked_list_1)
    linked_list_1.print_list('After 1')

    linked_list_2 = LinkedList()
    for e in l:
        linked_list_2.append(e)
    linked_list_2.print_list('Before 2')
    solution_2(linked_list_2)
    linked_list_2.print_list('After 2')

    linked_list_3 = LinkedList()
    for e in l:
        linked_list_3.append(e)
    linked_list_3.print_list('Before 3')
    solution_3(linked_list_3)
    linked_list_3.print_list('After 3')
