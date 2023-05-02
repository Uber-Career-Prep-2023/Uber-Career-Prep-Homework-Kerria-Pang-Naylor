# Strategy: Generic search
# Time: 20 minutes
# Space Complexity: O(1)
# Time Complexity: O(logn) to O(n)
from BinarySearchTree import *
def floorInBST(root, val): # if no floor exists (i.e., all nodes are greater than val or tree is empty) return None
    if not root:
        return None
    elif root.val == val:
        return root.val
    elif root.val > val: # must be in left child
        return floorInBST(root.left, val)
    else: # can be in either child
        right_candidate = floorInBST(root.right, val)
        if right_candidate:
            return right_candidate
        else:
            return root.val
        

if __name__ == "__main__":
    # empty tree/tree w/o a floor
    root0 = None
    assert(floorInBST(root0, 1) == False)

    bst = BinarySearchTree()
    bst.insert(5)
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    assert(floorInBST(bst.root, 0) == None)

    # successful find
    bst2 = BinarySearchTree()
    bst2.insert(5)
    for num in [3,1,4,7,6,8]:
        bst2.insert(num)
    assert(floorInBST(bst2.root, 2) == 1)
    assert(floorInBST(bst2.root, 9) == 8)

    # given example
    bst3 = BinarySearchTree()
    for num in [10,8,16,9,13,17,20]:
        bst3.insert(num)
    assert(floorInBST(bst3.root, 15) == 13)
    assert(floorInBST(bst3.root, 13) == 13)