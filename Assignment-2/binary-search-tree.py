# Node subclass
class Node:
    def __init__(self, val:int, right = None, left = None) -> None:
        self.val:int = val
        self.right = right
        self.left = left

class BinarySearchTree(Node):
    def __init__(self, startVal:int) -> None:
        self.root = Node(startVal)

    def min(self) -> int: # returns the minimum value in the BST
        ptr = self.root
        while ptr and ptr.left:
            ptr = ptr.left
        if ptr:
            return ptr.val
        else:
            return -1
    
    def max(self) -> int: # returns the maximum value in the BST
        ptr = self.root
        while ptr and ptr.right:
            ptr = ptr.right
        if ptr:
            return ptr.val
        else:
            return -1
        
    # returns a boolean indicating whether val is present in the BST
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
    def insert(self, val:int) -> None:
        if not self.contains(val):
            self.insertHelper(self.root, val)
    
    def insertHelper(self, ptr:Node, val:int) -> Node: 
        # Python does pass by reference for objects (I think, otherwise this has horrible space complexity. In hindsight I really should've done this in C+ :(.)
        if ptr is None:
            return Node(val)
        elif val < ptr.val:
            ptr.left = self.insertHelper(ptr.left, val)
        else:
            ptr.right = self.insertHelper(ptr.right, val)
        return ptr
    
    # deletes the Node with data val, if it exists 
    def delete(self, val:int) -> None:
        if self.contains(val):
            self.deleteHelper(self.root, val)
    
    def deleteHelper(self, ptr:Node, val:int):
        if ptr is None:
            return None
        if val < ptr.val:
            ptr.left = self.deleteHelper(ptr.left, val)
        elif val > ptr.val:
            ptr.right = self.deleteHelper(ptr.right, val)
        else:
            # leaf -> just remove
            if ptr.right is None and ptr.left is None:
                ptr = None
            elif ptr.left is None: 
                ptr = ptr.right
            
            elif ptr.right is None:    
                ptr = ptr.left

            else:
                # only right child or two children --> replace with min of right child
                replace = self.recursiveMin(ptr.right)
                print(replace)
                ptr.right = self.deleteHelper(ptr.right, replace)
                ptr.val = replace
        return ptr



    # def recursiveMax(self, ptr:Node) -> int:
    #     if ptr:
    #         if ptr.right:
    #             return self.recursiveMax(ptr.right)
    #         else:
    #             return ptr.val
    #     else:
    #         return -1
    
    def recursiveMin(self, ptr:Node) -> int:
        if ptr:
            if ptr.left:
                return self.recursiveMin(ptr.left)
            else:
                return ptr.val
        else:
            return -1
    

if __name__ == "__main__":
    bst = BinarySearchTree(5)
    print(bst.root.val)
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    for num in [3,1,4,7,6,8]:
        print(num, ":", bst.contains(num))
    bst.delete(5)
    assert(bst.root.val == 6)
    bst.delete(8)

    for num in [3,1,4,7,6,8]:
        print(num, ":", bst.contains(num))
    assert(bst.contains(5) == False)
    assert(bst.contains(8) == False)
   

