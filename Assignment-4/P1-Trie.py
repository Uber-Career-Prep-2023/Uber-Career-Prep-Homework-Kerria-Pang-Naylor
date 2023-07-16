"""
Question 1: Build a Trie

Implement a trie class, including the insert, search, and delete methods. Your class should adhere to the following API, adjusted appropriately for your language of choice.  

struct TrieNode {
   vector<struct TrieNode *> children; // a (resizable or fixed size) array of size 26
   bool validWord; // boolean to indicate if this node marks the end of a word
};

class Trie {
  struct TrieNode* root;

  void insert(string word); // adds a word to the trie
  bool isValidWord(string word); // returns a boolean indicating whether word is in the trie
  void remove(string word); // removes word, from the trie & deletes unused nodes
}

"""

# time taken : ~1 hr

from collections import deque
# Trie search complexity: O(M) where M is the maximum string length

# node struct
class TrieNode:
    def __init__(self) -> None:
        self.children:list = [None]*26 # list of "children" TrieNodes, each index corresponds to nth letter
        self.validWord:bool = False


# Trie object
class Trie(TrieNode):
    def __init__(self) -> None:
        self.root:TrieNode = TrieNode()
    

    def insert(self, word:str) -> None: # adds a word to the trie
        # Time Complexity: O(n) (n = length of word)
        # Time Complexity: O(1)
        curr_node = self.root

        for letter in word:
            letter_i = ord(letter)-97 # convert letter to index within children
                 
            if not curr_node.children[letter_i]: # doesn't have letter, add to trie
                new_node = TrieNode()
                curr_node.children[letter_i] = new_node
            
            curr_node = curr_node.children[letter_i]
        curr_node.validWord = True # mark last letter as valid


    # Time Complexity: O(n) (n = length of word)
    # Time Complexity: O(1)
    def isValidWord(self, word:str) -> bool: # returns a boolean indicating whether word is in the trie
        curr_node = self.root
        for letter in word:
            letter_i = ord(letter)-97 # convert letter to index within children

            if not curr_node.children[letter_i]: # keep going down trie unless letter isn't found
                return False
            curr_node = curr_node.children[letter_i]

        return curr_node.validWord
    
    def remove(self, word:str) -> None: 
        # recursive strategy. Get to end, of trie, delete leaves until you get to one that another word relies on.
        if not self.isValidWord(word): return

        def removeHelper(root:TrieNode, word:str, depth = 0) -> None:
            if not root: return None

            if depth == len(word): # at where word should be
                if root.validWord: 
                    root.validWord = False
                if root.children == [None]*26: 
                    del root
                    root = None
                return root
                
            # otherwise go down trie
            i = ord(word[depth])-97
            root.children[i] = removeHelper(root.children[i], word, depth = depth + 1)

            # if has not children
            if root.children == [None]*26 and not root.validWord:
                del root
                root = None
            return root

        removeHelper(self.root, word, 0)
            

    def removeV2(self, word:str) -> None: # when I misunderstood the problem to mean deleting all the nodes
        if not self.isValidWord(word):
            return # do nothing if word isn't in Trie
        
        # otherwise, make way down trie and delete nodes that have no children after deletion of relevant child
        curr_node = self.root

        for letter in word:
            letter_i = ord(letter)-97 # convert letter to index within children
            
            next_node = curr_node.children[letter_i] # save child (python stores things in list by reference)

            curr_node.children[letter_i] = None # delete child from list

            # if all children are none, delete curr_node
            if curr_node.children == [None]*26:
                del curr_node

            curr_node = next_node

    def generateString(self): # generate string version of Trie
        q = deque()

        if not self.root: # null case
            return ""
        
        q.appendleft(self.root)

        string = ""

        while q:
            curr_node = q.pop()
            # assume character for root has already been added
            string += "("
            for i in range(len(curr_node.children)):
                if curr_node.children[i]:
                    string += chr(97+i) + ", "
                    q.appendleft(curr_node.children[i]) # put TrieNode object on queue
            string += ")"
        return string
    

"""
------------------------------
            TESTS
------------------------------
"""

def insertAndValidWordTests():
    test0 = Trie()
    test0.insert("a")
    assert(test0.generateString() == "(a, )()")
    assert(test0.isValidWord("a"))
    
    test0.insert("apple")
    assert(test0.generateString() == "(a, )(p, )(p, )(l, )(e, )()")
    assert(test0.isValidWord("a"))
    assert(test0.isValidWord("apple"))

    test0.insert("apply")
    assert(test0.generateString() == "(a, )(p, )(p, )(l, )(e, y, )()()")
    assert(test0.isValidWord("a"))
    assert(test0.isValidWord("apple"))
    assert(test0.isValidWord("apply"))

    test0.insert("awesome")
    assert(test0.generateString() == "(a, )(p, w, )(p, )(e, )(l, )(s, )(e, y, )(o, )()()(m, )(e, )()")
    assert(test0.isValidWord("a"))
    assert(test0.isValidWord("apple"))
    assert(test0.isValidWord("apply"))
    assert(test0.isValidWord("awesome"))

    test0.insert("badminton")
    assert(test0.generateString() == "(a, b, )(p, w, )(a, )(p, )(e, )(d, )(l, )(s, )(m, )(e, y, )(o, )(i, )()()(m, )(n, )(e, )(t, )()(o, )(n, )()")
    assert(test0.isValidWord("a"))
    assert(test0.isValidWord("apple"))
    assert(test0.isValidWord("apply"))
    assert(not test0.isValidWord("app"))
    assert(test0.isValidWord("badminton"))

def removeTests():
    test0 = Trie()
    test0.insert("apple")
    test0.insert("apply")

    test0.remove("apple")
    test0.remove("badminton")
    assert(test0.generateString() == "(a, )(p, )(p, )(l, )(y, )()") # will inevitably delete apple as well
    
    test0.insert("badminton")
    test0.remove("badminton")
    assert(test0.generateString() == "(a, )(p, )(p, )(l, )(y, )()")

    test0.remove("apply")
    assert(test0.generateString() == "()")

insertAndValidWordTests()        
removeTests()


    
    
    