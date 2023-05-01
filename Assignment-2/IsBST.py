# Strategy: pre-order search
# Time: 10 minutes
# Space Complexity: O(n)
# Time Complexity: O(1)

from BinarySearchTree import BinarySearchTree
from BinarySearchTree import Node

def isBST(root:Node):
    if not root:
        return True
    else:
        right_subtree = True
        left_subtree = True
        if root.right:
            if root.val >= root.right.val:
                return False 
            else:
                right_subtree = isBST(root.right)
        if root.left:
            if root.val <= root.left.val:
                return False
            else: 
                left_subtree = isBST(root.left)
        return left_subtree and right_subtree
    

if __name__ == "__main__":
    # check empty
    root = None
    assert(isBST(root))
    
    # check for not BST
    root = Node(5)
    assert(isBST(root))
    root.right = Node(6)
    root.right.left = Node(7)
    root.left = Node(6)
    assert(isBST(root) == False)

    # check for BST
    bst = BinarySearchTree()
    bst.insert(5)
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    assert(isBST(bst.root))

    


