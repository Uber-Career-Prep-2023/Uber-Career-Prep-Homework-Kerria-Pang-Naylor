# Strategy: Fixed-Distance two pointer
# Time: 15 minutes
# Space Complexity: O(n)
# Time Complexity: O(1)

from SinglyLinkedList import Node
from SinglyLinkedList import makeList
from SinglyLinkedList import insertAtBack


def dedupSortedList(startNode:Node):
    left = startNode
    right = startNode.next
    if right:
        while right.next:
            if left.data == right.data:
                left.next = right.next # delete node
            left = left.next
            right = right.next
    return startNode


if __name__ == "__main__":
    list1 = Node(0)
    for val in [1,1,2,3,4]:
        insertAtBack(list1, val)
    dedupSortedList(list1)
    assert([0, 1, 2, 3, 4] == makeList(list1))

    list2 = Node(0)
    for val in [1,2,3,4]:
        insertAtBack(list2, val)
    dedupSortedList(list2)
    assert([0, 1, 2, 3, 4] == makeList(list1))

    list3 = Node(0)
    dedupSortedList(list3)
    assert([0] == makeList(list3))
