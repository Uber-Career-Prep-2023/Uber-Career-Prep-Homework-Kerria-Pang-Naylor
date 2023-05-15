# Strategy: Two pointer, forward backward
# Time: 15 minutes
# Space Complexity: O(1)
# Time Complexity: O(n) (assume that we're only given first pointer)

from DoublyLinkedList_2 import *
import pdb

def isPalindrome(startNode:Node):
    # empty LL
    if not startNode:
        return True
    
    # first get to last node
    leftPtr = startNode
    rightPtr = startNode
    while rightPtr.next:
        rightPtr = rightPtr.next

    # bring pointers togethers
    while not (leftPtr is rightPtr) and not (leftPtr.next is rightPtr):
        if leftPtr.data != rightPtr.data:
            return False
        leftPtr = leftPtr.next
        rightPtr = rightPtr.prev

    return True


if __name__ == "__main__":
    # check not palindrom
    list1 = Node(0)
    for val in [1,2,3]:
        insertAtBack(list1,val)

    assert(isPalindrome(list1) == False)

    # check palindrome = (odd number)
    list2 = Node(0)
    for val in [1,2,3,2,1,0]:
        insertAtBack(list2,val)
    assert(isPalindrome(list2))

    # check palindrome (even number)
    list2 = Node(0)
    for val in [1,2,3,3,2,1,0]:
        insertAtBack(list2,val)
    assert(isPalindrome(list2))

    list3 = Node(0)
    assert(isPalindrome(list3))