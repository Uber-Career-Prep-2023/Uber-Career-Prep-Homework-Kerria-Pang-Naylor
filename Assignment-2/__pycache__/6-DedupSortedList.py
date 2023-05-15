# Strategy: Fixed-Distance two pointer
# Time: 15 minutes
# Space Complexity: O(1)
# Time Complexity: O(n)

from SinglyLinkedList_1 import Node, makeList, insertAtBack



def dedupSortedList(startNode:Node):
    if not startNode:
        return None
    
    left = startNode
    right = startNode.next
    
    if right:  # return startNode if right is None, cleaner
        while right.next:
            if left.data == right.data:
                left.next = right.next # delete node 
                right.next = None # free memory
            left = left.next
            right = left.next
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

    #Always watch out for nil requests
    dedupSortedList(None)
