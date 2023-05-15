import pdb

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None # reference to next node

# creates new Node with data val at front; returns new head
# Space: O(1)
# Time: O(1)
def insertAtFront(head:Node, val:int) -> Node:
    newNode = Node(val)
    newNode.next = head
    return newNode


# creates new Node with data val at end
# Space: O(1)
# Time: O(n)
def insertAtBack(head:Node, val:int) -> None:
    newNode = Node(val)
    
    ptrNode = head
    if not head:
        return newNode 
    while ptrNode.next:
        ptrNode = ptrNode.next
    ptrNode.next = newNode

# creates new Node with data val after Node loc (otherwise appends to end)
# Space: O(1)
# Time: O(n)
def insertAfter(head:Node, val:int, loc:Node) -> Node:
    newNode = Node(val)

    ptr = head
    while ptr and (ptr is loc) == False:
        ptr = ptr.next

    if ptr is loc: # replace if loc is list, else do nothing
        oldNext = ptr.next
        ptr.next = newNode # replace next
        newNode.next = oldNext

# removes first Node; returns new head
# Space: O(1)
# Time: O(1)
def deleteFront(head:Node) -> Node:
    if head:
        newHead = head.next
        head.next = None # cutoff old head
        return newHead

# removes last Node
# Space: O(1)
# Time: O(n)
def deleteBack(head:Node):
    if not head or (head and not head.next): # case where one node or no nodes
        head = None
        return
    
    ptr = head
    while ptr.next and ptr.next.next: # check ptr.next to catch nullptr bugs
        ptr = ptr.next

    # when ptr.next.next == None, ptr is second to last --> cutoff
    ptr.next = None
    #return head
    

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
# rename ptr and ptr1 to start and end or begin and end.
def reverseIterative(head:Node) -> Node:
    if not head:
        return None
    
    left = head
    right = head.next
    head.next = None
    while right:
        save_next = right.next
        right.next = left

        # iterate pointers
        left = right
        right = save_next
    return left

# reverses the linked list recursively
# Space: O(1)
# Time: O(n)
def reverseRecursive(head:Node) -> Node:
    if (head == None):
        return head
         
    if head.next:         
        reverseNode = reverseRecursive(head.next)
        head.next.next = head
        head.next = None
        return reverseNode
    else:
        return head




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
    TestInsertFront()
    TestInsertBack()
    TestDeleteFront()
    TestDeleteBack()
    TestReverseIterative()
    TestReverseRecursive()