from implementations.linked_list import LinkedList


def solution(number_1: LinkedList, number_2: LinkedList) -> LinkedList:
    # Worst Case -> Time: O(n²) due to append in 'result_linked_list', Space: O(n)
    # Reverse Order. Ex: 1 -> 2 -> 3 == 321
    result_linked_list = LinkedList()
    current_1 = number_1.head
    current_2 = number_2.head
    carry = 0
    while current_1 and current_2:
        s = current_1.data + current_2.data + carry
        carry = s // 10
        digit = s % 10
        result_linked_list.append(digit)
        current_1 = current_1.next
        current_2 = current_2.next

    if current_1 is None and current_2 is None:
        return result_linked_list

    current = current_1 if current_1 is not None else current_2
    while current:
        s = current.data + carry
        carry = s // 10
        digit = s % 10
        result_linked_list.append(digit)
        current = current.next

    return result_linked_list


if __name__ == '__main__':
    l1 = [6, 1, 7]
    l2 = [2, 9, 5]
    number_1_reverse = LinkedList()
    number_2_reverse = LinkedList()
    for digit in l1:
        number_1_reverse.insert(digit)
    for digit in l2:
        number_2_reverse.insert(digit)

    number_1_reverse.print_list()
    number_2_reverse.print_list('+')
    solution(number_1_reverse, number_2_reverse).print_list('=')
