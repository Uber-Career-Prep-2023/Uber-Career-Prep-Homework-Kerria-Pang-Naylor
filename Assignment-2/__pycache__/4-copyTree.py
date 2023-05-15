# Strategy: pre-order search
# Time: 10 minutes
# Space Complexity: O(n)
# Time Complexity: O(n)
from BinarySearchTree_3 import Node, BinarySearchTree

import pdb

def copyTree(bst):
    copyTree = BinarySearchTree()

    #read more about passing by reference in python
    def addNode(root:Node): # weird gross python high global variable/higher order function property
        if root:
            copyTree.insert(root.val)
            addNode(root.left)
            addNode(root.right)
    addNode(bst.root)

    return copyTree


if __name__ == "__main__":
    def equality_checker(bstNode, bstNodeCopy):
        if (bstNode and bstNodeCopy == None) or (bstNodeCopy and bstNode == None):
            return False
        elif (bstNode == None and bstNode == None): # can't compare addresses of NoneType
            return True
        else:
            print("bstNode: ", bstNode.val)
            print("bstNodeCopy: ", bstNodeCopy.val)
            print("deepcopy: ", (bstNode is bstNodeCopy), "\n")
            equal_copy = (bstNode.val == bstNodeCopy.val) and (bstNode is bstNodeCopy) == False
            if equal_copy:
                return equality_checker(bstNode.left, bstNodeCopy.left) and equality_checker(bstNode.right, bstNodeCopy.right)
            else:
                return False

# Create functions for test as well

    # 1 node
    bst = BinarySearchTree()
    bst.insert(4)
    bstcopy = copyTree(bst)
    assert(equality_checker(bst.root, bstcopy.root))

    # balanced tree
    bst.insert(10)
    bst.insert(3)
    bst.insert(1)

    bstcopy2 = copyTree(bst)
    assert(equality_checker(bst.root, bstcopy2.root))

    # stick
    stick = BinarySearchTree()
    stick.insert(1)
    stick.insert(2)
    stick.insert(3)
    stick.insert(4)
    stick.insert(5)
    stickcopy = copyTree(stick)
    assert(equality_checker(stick.root, stickcopy.root))


    


