# Node subclass
class Node:
    def __init__(self, val:int, right = None, left = None) -> None:
        self.val:int = val
        self.right = right
        self.left = left

class BinarySearchTree(Node):
    
    def __init__(self) -> None:
        self.root = None
        pass

    # Space: O(1)
    # Time: O(log(n)) [worst case O(n)]
    def min(self) -> int: # returns the minimum value in the BST
        if not self.root:
            return -1
        ptr = self.root
        while ptr.left:
            ptr = ptr.left
        return ptr.val

        
    # Space: O(1)
    # Time: O(log(n)) [worst case O(n)]
    def max(self) -> int: # returns the maximum value in the BST
        if not self.root:
            return -1
        ptr = self.root
        while ptr and ptr.right: 
            ptr = ptr.right
        return ptr.val
        
    # returns a boolean indicating whether val is present in the BST
    # Space: O(1)
    # Time: O(log(n)) [worst case O(n)]
    def contains(self, val:int) -> bool: 
        return self.containsHelper(self.root, val)
    
    def containsHelper(self, ptr:Node, val:int) -> bool:
        if not ptr:
            return False
        elif val == ptr.val:
            return True
        elif val < ptr.val:
            return self.containsHelper(ptr.left, val)
        else:
            return self.containsHelper(ptr.right, val)
    
    # creates a new Node with data val in the appropriate location
    # Space: O(1)
    # Time: O(log(n)) [worst case O(n)]
    def insert(self, val:int) -> None:
        self.root = self.insertHelper(self.root, val)
    
    def insertHelper(self, ptr:Node, val:int) -> Node: 
        # Python does pass by reference for objects 
        if ptr is None:
            return Node(val)
        elif val < ptr.val:
            ptr.left = self.insertHelper(ptr.left, val)
        elif val > ptr.val:
            ptr.right = self.insertHelper(ptr.right, val)
        return ptr
    
    # deletes the Node with data val, if it exists 
    # Space: O(1)
    # Time: O(log(n)) [worst case O(n)]
    def delete(self, val:int) -> None:
        self.deleteHelper(self.root, val)
    
    def deleteHelper(self, ptr:Node, val:int):
        if ptr is None:
            return None
        if val < ptr.val:
            ptr.left = self.deleteHelper(ptr.left, val)
        elif val > ptr.val:
            ptr.right = self.deleteHelper(ptr.right, val)
        else:
            if ptr.right is None and ptr.left is None:
                ptr = None
            elif ptr.left is None: 
                ptr = ptr.right
            elif ptr.right is None:    
                ptr = ptr.left
            else:
                replace = self.recursiveMin(ptr.right)
                ptr.right = self.deleteHelper(ptr.right, replace)
                ptr.val = replace
        return ptr
    
    def recursiveMin(self, ptr:Node) -> int: # helper
        if ptr:
            if ptr.left:
                return self.recursiveMin(ptr.left)
            else:
                return ptr.val
        else:
            return -1


"""
---------------------
       TESTS
---------------------
"""

def TestMinimum():
    # empty tree
    bst = BinarySearchTree()
    assert(bst.min() == -1)

    # 1 node tree
    bst = BinarySearchTree()
    bst.insert(5)
    assert(bst.min() == 5)

    # 7 node tree
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    assert(bst.min() == 1)

def TestMaximum():
    # empty tree
    bst = BinarySearchTree()
    assert(bst.max() == -1)

    # 1 node tree
    bst = BinarySearchTree()
    bst.insert(5)
    assert(bst.max() == 5)

    # 7 node tree
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    assert(bst.max() == 8)

def TestContains():
    # empty tree
    bst = BinarySearchTree()
    assert(bst.contains(1) == False)

    # 1 node tree
    bst = BinarySearchTree()
    bst.insert(5)
    assert(bst.contains(5))

    # 7 node tree
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    assert(bst.contains(5))
    assert(bst.contains(3))
    assert(bst.contains(1))
    assert(bst.contains(4))
    assert(bst.contains(7))
    assert(bst.contains(6))
    assert(bst.contains(8))

def TestDelete():
    # empty tree
    bst = BinarySearchTree()
    assert(bst.delete(1)== None)

    # 1 node tree
    bst = BinarySearchTree()
    bst.insert(5)
    assert(bst.delete(5) == None)

    # 7 node tree
    bst = BinarySearchTree()
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    bst.delete(3)
    assert(bst.contains(3) == False)
    
    bst.delete(5)
    assert(bst.contains(5) == False)


if __name__ == "__main__":
    TestMinimum()
    TestMaximum()
    TestContains()
    TestDelete()

   

