from implementations.linked_list import LinkedList, Node


def solution(node: Node) -> None:
    if node is None or node.next is None:
        raise ValueError('Cannot remove the head or the last node.')

    node.data, node.next = node.next.data, node.next.next


if __name__ == '__main__':
    l = [i for i in range(10)]
    linked_list = LinkedList()
    for e in l:
        linked_list.append(e)
    linked_list.print_list('Before')
    solution(linked_list.head.next.next.next)
    linked_list.print_list('After')
