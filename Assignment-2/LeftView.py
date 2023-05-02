# Strategy: pre-order search
# Time: 30 minutes
# Space Complexity: O(n)
# Time Complexity: O(n)

from BinarySearchTree import *
import pdb


def leftView(rootNode):
    leftView = []

    def leftViewRecursive(node:Node, level:int, levels_visited) -> None: # accesses outside
        #pdb.set_trace()

        """ 
        Update leftView list if level has been visited
        root = root node
        level = distance from root
        """
        if node:
            to_add = False
            if level > levels_visited:
                leftView.append(node.val)
                levels_visited += 1 
            levels_visited = leftViewRecursive(node.left, level + 1, levels_visited) # first update levels visited with 
            levels_visited = leftViewRecursive(node.right, level + 1, levels_visited)

        return levels_visited
    
    leftViewRecursive(rootNode, 0, -1)
    return leftView

if __name__ == "__main__":
    # empty tree
    root0 = None
    assert([] == leftView(root0))

    # simple tree
    root1 = Node(5)
    root1.left = Node(1)
    root1.right = Node(6)
    assert([5,1] == leftView(root1))

    # complicated tree (should als work with normal non-search binary binary)
    bst = BinarySearchTree()
    bst.insert(5)
    for num in [3,1,4,7,6,8]:
        bst.insert(num)
    assert([5,3,1] ==leftView(bst.root))
    
    
    # stick
    bst2 = BinarySearchTree()    
    for num in[5,1,6,7,8,9,10]:
        bst2.insert(num)
    assert([5,1,7,8,9,10] ==leftView(bst2.root))


