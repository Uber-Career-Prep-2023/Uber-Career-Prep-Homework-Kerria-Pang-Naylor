# Strategy: Hash the nodes
# Time: 15 minutes
# Space Complexity: O(1)
# Time Complexity: O(n)

from SinglyLinkedList_1 import *

def disconnectCycle(startNode):
    past_nodes = set() # hashset of *references* to past visited nodes
    ptr = startNode

    while ptr:
        past_nodes.add(ptr)
        if ptr.next in past_nodes: # break 
            ptr.next = None
        ptr = ptr.next
    return startNode

if __name__ == "__main__":
    # cycle w/o repeating values
    n1 = Node(0)
    n1.next = Node(1)
    saveNode = n1.next # save node(1)
    n1.next.next = Node(2)
    n1.next.next.next = Node(3)
    n1.next.next.next.next = saveNode
    list1 = disconnectCycle(n1)
    try:
        assert(makeList(list1) == [0,1,2,3]) # would run forever if there was a loop
    except:
        print("Cycle not broken")

    # cycle w/ repeating values
    n1 = Node(0)
    n1.next = Node(1)
    saveNode = n1.next # save node(1)
    n1.next.next = Node(1)
    n1.next.next.next = Node(2)
    n1.next.next.next.next = Node(3)
    n1.next.next.next.next.next = saveNode
    list1 = disconnectCycle(n1)
    try:
        assert(makeList(list1) == [0,1,1,2,3]) # would run forever if there was a loop
    except:
        print("Cycle broken")
    n1 = Node(0)
    n1.next = n1
    list1 = disconnectCycle(n1)
    assert(makeList(list1) == [0])
