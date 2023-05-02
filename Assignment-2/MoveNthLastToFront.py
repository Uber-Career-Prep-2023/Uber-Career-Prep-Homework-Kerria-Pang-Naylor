# Strategy: Two pointer (variable length)
# Time: 15 minutes
# Space Complexity: O(n)
# Time Complexity: O(n)
from SinglyLinkedList import *



def moveToFront(startNode:Node, k:int):
    length_ = length(startNode)
    ptr = startNode

    if length_-k-1 < 0: # invalid, return same linked list
        return startNode
    
    for i in range(length_-k-1):
        print(ptr.data)
        ptr = ptr.next

    new_front = ptr.next
    ptr.next = ptr.next.next
    new_front.next = startNode
    return new_front


if __name__ == "__main__":
    # check valid moveToFront
    list1 = Node(0)
    for val in [1,2,3]:
        insertAtBack(list1,val)
    list1 = moveToFront(list1, 1)
    assert([3,0,1,2] == makeList(list1))

    # check invalid moveToFront
    list2 = Node(0)
    for val in [1,2,3]:
        insertAtBack(list2,val)
    list2 = moveToFront(list2, 5)
    assert([0,1,2,3] == makeList(list2))


