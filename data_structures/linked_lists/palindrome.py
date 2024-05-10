from implementations.linked_list import LinkedList


def solution(linked_list: LinkedList) -> bool:
    # Worst Case -> Time: O(n), Space: O(n)
    temp_linked_list = LinkedList()
    current = linked_list.head
    while current:
        # Insert at the beginning to reverse order
        # Append will mantain the order
        temp_linked_list.insert(current.data)
        current = current.next

    temp_linked_list.print_list('TEMP')
    current_1 = linked_list.head
    current_2 = temp_linked_list.head
    while current_1 and current_2:
        if current_1.data != current_2.data:
            return False
        current_1 = current_1.next
        current_2 = current_2.next

    return True

if __name__ == '__main__':
    l1 = [1, 2, 3, 4]
    l2 = [4, 2, 2, 4]
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for e in l1:
        linked_list_1.append(e)
    for e in l2:
        linked_list_2.append(e)
    linked_list_1.print_list('L1')
    print(solution(linked_list_1))
    linked_list_2.print_list('L2')
    print(solution(linked_list_2))
