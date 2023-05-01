import pdb

class Node:
    def __init__(self, data, next = None, prev = None) -> None:
        self.data = data
        self.next = next # reference to next node
        self.prev = prev

# creates new Node with data val at front; returns new head
def insertAtFront(head:Node, val:int) -> Node:
    newNode = Node(val, next = head)
    newNode.next.prev = newNode
    return newNode


# creates new Node with data val at end
def insertAtBack(head:Node, val:int) -> None:
    newNode = Node(val)
    
    ptrNode = head
    while ptrNode.next:
        ptrNode = ptrNode.next
    ptrNode.next = newNode
    newNode.prev = ptrNode

# creates new Node with data val after Node loc (otherwise do nothing
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
def deleteFront(head:Node) -> Node:
    head.next.prev = None
    return head.next

# removes last Node
def deleteBack(head:Node) -> None:
    ptr = head
    ptr2 = head.next
    while ptr2.next:
        ptr = ptr.next
        ptr2 = ptr2.next
    
    ptr.next = None

# returns length of list
def length(head) -> int:
    if head:
        return 1 + length(head.next)
    else:
        return 0

# reverses the linked list iteratively
def reverseIterative(head:Node) -> Node:
    ptr = head
    ptr2 = head.next
    ptr.next = None # create new end
    while ptr2:
        save_next = ptr2.next
        ptr2.next = ptr # reverse links
        ptr.prev = ptr2    

        # iterate pointers
        ptr = ptr2
        ptr2 = save_next
    return ptr

# reverses the linked list recursively
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



if __name__ == "__main__":
    # technically didn't ask me to test anything but I added these 
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

