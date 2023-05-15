# Strategy: pre-order search
# Time: 10 minutes
# Space Complexity: O(1)
# Time Complexity: O(n)

from BinarySearchTree_3 import BinarySearchTree, Node

def isBST(root:Node):
    if not root:
        return True
    # To be a BST, must satisfy:
    # (1) right and left subtrees must be BST (2) min of right > root (3) max of left < root
    right_subtree = True
    left_subtree = True

    if root.right:
        if root.val >= root.right.val:
            return False 
        if minHelper(root.right) <= root.val:
            return False
        right_subtree = isBST(root.right)

    if root.left:
        if root.val <= root.left.val:
            return False
        if maxHelper(root.left) >= root.val:
            return False
        left_subtree = isBST(root.left)
  
    return left_subtree and right_subtree

def minHelper(node:Node) -> int:
    if not node:
        return -1
    while node.left:
        node = node.left
    return node.val

def maxHelper(node:Node) -> int:
    if not node:
        return 99999
    while node.right:
        node = node.right
    return node.val

"""
--------------------
       TESTS
--------------------
"""
#        5
#      3      6
#    1   9
def testBug():
    five = Node(5)
    three = Node(3)
    six = Node(6)
    one = Node(1)
    nine = Node(9)

    five.left = three
    five.right = six

    three.left = one
    three.right = nine
    assert(isBST(five) == False)

    # transverse with allowed MIN and MAX set for each level

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

    # check when maximum of left is greater than root
    five = Node(5)
    three = Node(3)
    six = Node(6)
    one = Node(1)
    nine = Node(9)

    five.left = three
    five.right = six

    three.left = one
    three.right = nine
    assert(isBST(five) == False)
    testBug()

    # check when minimum of right is greater than root
    #     5
    #  3      9
    #       1
    five = Node(5)
    three = Node(3)
    one = Node(1)
    nine = Node(9)

    five.right = nine
    nine.left = one
    five.left = three
    assert(isBST(five) == False)

    


