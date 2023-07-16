"""
Question 6: WordBreak
Given a string of characters without spaces and a dictionary of valid words, determine if it can be
 broken into a list of valid words by adding spaces. 

Dictionary:

Elf
Go
Golf
Man
Manatee
Not
Note
Pig
Quip
Tee
Teen


Input: mangolf
Output: True (“man”, “golf”)

Input: manateenotelf
Output: True (“manatee”, “not”, “elf”)

Input: quipig
Output: False
"""

# Strategy: bottom-up tabulation
# if you can make word of first k words, AND can make words from rest word[k:] (recurse), then return true
# Edge case: can fit multiple words (i.e., word is prefix of longer word), 

# Time taken: ~15 minutes

# k = number of words, n = length of string
# Time: O(k*n)
# Space: O(k*n)


def wordBreak(s: str, wordDict: list[str]) -> bool:
    lengths = [len(word) for word in wordDict] # all lengths of words, O(n)
    words=set(wordDict) #so O(1) for access
    memo = {} # length of substring to return
    def rec(s):
        # memo + base cases
        if len(s) in memo:
            return memo[len(s)]

        if s == "":
            return True
        if s in wordDict:
            return True
        
        possible_rest = []

        # go through possible starting words (hence O(k*n))
        for k in lengths:
            if s[:k] in words:
                possible_rest.append(rec(s[k:]))

        if True in possible_rest: # if one prefix works, then wordBreak holds
            memo[len(s)] = True
            return True
        
        memo[len(s)] = False
        return False
    
    return rec(s)

"""
------------------------------
            TESTS
------------------------------
"""
# NOTE: this solution passes all test cases on https://leetcode.com/problems/word-break/description/

def tests():
    assert(wordBreak("leetcode", ["leet","code"]))
    assert(wordBreak("applepenapple", ["apple","pen"]))
    assert(not wordBreak("catsandog",["cats","dog","sand","and","cat"]))
    assert(wordBreak("bccdbacdbdacddabbaaaadababadad",["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]))

tests()