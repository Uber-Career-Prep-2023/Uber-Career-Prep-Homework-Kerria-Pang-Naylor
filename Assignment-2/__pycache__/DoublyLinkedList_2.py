import pdb

class Node:
    def __init__(self, data, next = None, prev = None) -> None:
        self.data = data
        self.next = next # reference to next node
        self.prev = prev

# creates new Node with data val at front; returns new head
# Space: O(1)
# Time: O(1)
def insertAtFront(head:Node, val:int) -> Node:
    newNode = Node(val, next = head)
    if head:
        newNode.next.prev = newNode
    return newNode


# creates new Node with data val at end
# Space: O(1)
# Time: O(n)
def insertAtBack(head:Node, val:int) -> None:
    newNode = Node(val)
    if not head: # empty case
        head = newNode
        return head
    
    ptrNode = head
    while ptrNode.next:
        ptrNode = ptrNode.next
    ptrNode.next = newNode
    newNode.prev = ptrNode


# creates new Node with data val after Node loc (otherwise do nothing
# Space: O(1)
# Time: O(n)
def insertAfter(head:Node, val:int, loc:Node) -> Node:
    newNode = Node(val)

    ptr = head
    while ptr and (ptr is loc) == False:
        ptr = ptr.next

    if ptr:
        oldNext = ptr.next
        ptr.next = newNode # replace next
        newNode.next = oldNext
        oldNext.prev = newNode

# removes first Node; returns new head
# Space: O(1)
# Time: O(1)
def deleteFront(head:Node) -> Node:
    if not head or not head.next:
        return None
    head.next.prev = None
    return head.next

# removes last Node
# Space: O(1)
# Time: O(n) (we weren't allowed to have a class for this implementation so there's no shortcut pointer to the back of the list)
# can do this with only one pointer, since you can navigate backward and forward with only one pointer
#confusing logic, incrementing both ptr and ptr1. Should increment only one and assign ptr = ptr2 or vice versa
# bug head is only Node
# Also do ptr2.prev = None to disconnect ptr2
def deleteBack(head:Node) -> None:
    if not head:
        return None
    if not head.next:
        head.next.prev = None
        head.next = None
        return head
    
    ptr = head
    while ptr.next.next:
        ptr = ptr.next
    # cutoff last node
    ptr.next.prev = None 
    ptr.next = None
    return head

# returns length of list
# Space: O(1)
# Time: O(n)
def length(head) -> int:
    if head:
        return 1 + length(head.next)
    else:
        return 0

# reverses the linked list iteratively
# Space: O(1)
# Time: O(n)
def reverseIterative(head:Node) -> Node:
    if not head: 
        return None
    left = head
    right = head.next
    left.next = None # create new end
    while right:
        save_next = right.next
        right.next = left # reverse links
        left.prev = right    

        # iterate pointers
        left = right
        right = save_next
    return left

# reverses the linked list recursively
# Space: O(1)
# Time: O(n)
def reverseRecursive(head:Node) -> Node:
    if (head == None) or (head.next == None):
        return head
    else:
        last = head.next # this is what will be the second to last node
        reverseNode = reverseRecursive(head.next)
        
        # adjust pointers
        last.next = head
        head.prev = last
        head.next = None
        return reverseNode
    



# makes returns list form of linked list, testing purposes
def makeList(head:Node) -> list:
    arr = []
    ptr = head
    while ptr:
        arr.append(ptr.data)
        ptr = ptr.next
    return arr

"""
---------------------
       TESTS
---------------------
"""

def TestInsertFront():
    # empty case
    head = None
    head = insertAtFront(head, 1)
    assert(makeList(head) == [1])
    assert(length(head) == 1)

    # 1 node
    head = Node(0)
    head = insertAtFront(head, 1)
    assert(makeList(head) == [1,0])
    assert(length(head) == 2)

    # 4 nodes
    head3 = Node(0)
    insertAtBack(head3, 1)
    insertAtBack(head3, 2)
    insertAtBack(head3, 3)
    assert(length(head3) == 4)
    head3 = insertAtFront(head3, 0)
    assert(makeList(head3) == [0,0,1,2,3])
    assert(length(head3) == 5)

def TestInsertBack():
    # empty case
    head = None
    head = insertAtBack(head, 1)
    assert(makeList(head) == [1])

    # 1 node
    head = Node(0)
    insertAtBack(head, 1)
    assert(makeList(head) == [0,1])

    # 4 nodes
    head3 = Node(0)
    head3 = insertAtFront(head3, 1)
    head3 = insertAtFront(head3, 2)
    head3 = insertAtFront(head3, 3)
    insertAtBack(head3,-1)
    assert(makeList(head3) == [3,2,1,0,-1])

def TestDeleteFront():
    # empty case
    head = None
    head = deleteFront(head)
    assert(head == None)

    # 1 node
    head = Node(0)
    head = deleteFront(head)
    assert(head == None)

    # 4 nodes
    head3 = Node(0)
    insertAtBack(head3, 1)
    insertAtBack(head3, 2)
    insertAtBack(head3, 3)
    head3 = deleteFront(head3)
    assert(makeList(head3) == [1,2,3])

def TestDeleteBack():
    # empty case
    head = None
    head = deleteBack(head)
    assert(head == None)


    # one node case
    head1 = Node(2)
    head1 = deleteBack(head)
    assert(head1 == None)

    # 4 long node case
    head3 = Node(0)
    insertAtBack(head3, 1)
    insertAtBack(head3, 2)
    insertAtBack(head3, 3)
    deleteBack(head3)
    assert(makeList(head3) == [0,1,2])

def TestReverseIterative():
    # empty case 
    head = None
    reversed = reverseIterative(head)
    assert(reversed == None)

    # 1 node
    head = Node(2)
    reversed = reverseIterative(head)
    assert(head == reversed)

    # 4 nodes
    head3 = Node(0)
    insertAtBack(head3, 1)
    insertAtBack(head3, 2)
    insertAtBack(head3, 3)
    reversed = reverseIterative(head3)
    assert(makeList(reversed) == [3,2,1,0])

def TestReverseRecursive():
    # empty case 
    head = None
    reversed = reverseRecursive(head)
    assert(reversed == None)

    # 1 node
    head = Node(2)
    reversed = reverseRecursive(head)
    assert(head == reversed)

    # 4 nodes
    head3 = Node(0)
    insertAtBack(head3, 1)
    insertAtBack(head3, 2)
    insertAtBack(head3, 3)
    reversed = reverseRecursive(head3)
    assert(makeList(reversed) == [3,2,1,0])

# for testing it's better to isolate and name each test
# improves readability and troubleshooting
if __name__ == "__main__":
    TestInsertFront() # tests length() as well
    TestInsertBack() # tests length() as well
    TestDeleteFront()
    TestDeleteBack()
    TestReverseIterative()
    TestReverseRecursive()

    # Extra (technically didn't ask me to test anything but I added these)
    head = Node(2)
    print("[2]", makeList(head))
    assert(length(head) == 1)
    insertAtBack(head, 3)
    print("[2, 3]", makeList(head))
    assert(length(head) == 2)
    
    newHeadSave = insertAtFront(head, 1)
    newHead = insertAtFront(newHeadSave, 1)
    print("[1, 1, 2, 3]", makeList(newHead))
    assert(length(newHead) == 4)
    newHead2 = insertAtFront(newHead, 0)
    print("[0, 1, 1, 2, 3]", makeList(newHead2))
    insertAfter(newHead2, 99, newHeadSave)
    print("[0, 1, 1, 99, 2, 3]", makeList(newHead2))
    insertAfter(newHead2, 100, newHeadSave)
    print("[0, 1, 1, 100, 99, 2, 3]", makeList(newHead2))
    assert(length(newHead2) == 7)

    reversedHead = reverseIterative(newHead2)
    print("reversed: ", makeList(reversedHead))
    reversedAgain = reverseRecursive(reversedHead)
    print("new reversed: ", makeList(reversedAgain))
    assert(length(reversedAgain) == 7)


    l1 = deleteFront(reversedAgain)
    print("[1, 1, 100, 99, 2, 3]", makeList(l1))
    assert(length(l1) == 6)

    deleteBack(l1)
    print("[1, 1, 100, 99, 2]", makeList(l1))
    assert(length(l1) == 5)

