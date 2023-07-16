"""
Question 2: Boggle
Boggle is a word game in which players compete to find the most words on a square grid of random 
letters. Valid words must be at least three characters and formed from non-overlapping (i.e., a
position on the board can only be used once in a word) adjacent (including diagonal) letters. 
Given a Boggle board and a dictionary of valid words, return all valid words on the board.
"""
# STRATEGY: Trie + DFS + Generic Traversal. 
# Time complexity: O(k*m*n) where m*n is the number squares and k is the number of words 
#   because m*n (for generic traveral) + m*n*k (for every DFS worst case)
# Space Complexity: O(k) where k is the number of words (?? can I assume about how grid size scales with number of words?)

# Time taken: very long 


# TRIE CLASS
# ------------------------------------------------------------------------------------------------------------
# node struct
class TrieNode:
    def __init__(self, char = None) -> None:
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
            letter_i = ord(letter)-ord("a") # convert letter to index within children
                 
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

# ------------------------------------------------------------------------------------------------------------

# SOLUTION

def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    
    # 1 -- build Trie
    wordTrie = Trie()
    for word in words:
        wordTrie.insert(word)

    ROWS = len(board)
    COLS = len(board[0])
    
    allWords = []
    visited = set() # visited in board

    # 2 -- generic traversal + dfs
    # -------------------------------------------
    def dfs_found(row, col, curr_node, word):
        if not curr_node:
            return 
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited:
            return     
        
        if curr_node.validWord:
            allWords.append(word)
            wordTrie.remove(word)           

        # add to visited
        visited.add((row, col))

        for nrow, ncol in [(row+a[0], col+a[1]) for a in [(0,1),(0,-1),(1,0),(-1,0)]]:
            if not (nrow < 0 or ncol < 0 or nrow >= ROWS or ncol >= COLS):
                index = ord(board[nrow][ncol])-ord("a")
                if curr_node.children[index]:
                    dfs_found(nrow, ncol, curr_node.children[index], word+board[nrow][ncol])

        visited.remove((row,col))
    # -------------------------------------------

    # 3 -- Generic traversal
    for row in range(ROWS):
        for col in range(COLS):
            index = ord(board[row][col])-ord("a")
            if wordTrie.root.children[index]:
                dfs_found(row, col, wordTrie.root.children[index], board[row][col])
        
    return allWords


"""
------------------------------
            TESTS (taken from leetcode Word Search II)
------------------------------
"""
def test1():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    assert(findWords(board, words) == ["oath","eat"])

def test2():
    board = [["a","b"],["c","d"]]
    words = ["abcb"]    
    assert(findWords(board, words) == [])

def test3():
    board = [["a"]]
    words = ["a"]    
    assert(findWords(board, words) == ["a"])

test1()
test2()
test3()

