"""
Question 7: ReverseWords
Given a string, return the string with the order of the space-separated words reversed
"""

# Strategy: stack
# Time Complexity: O(n) -
# Space Complexity: O(n) - since strings are immutable
# Time: 20 min
# assume words are separated by single space, so two spaces results in an empty word

from collections import deque
def reverseWords(string):
    stack = deque()

    word = ""
    for chr in string:
        if chr == " ":
            stack.append(word)
            word = ""
        else:
            word += chr
    stack.append(word) # add last word

    # pop out of stack
    revWords = ""
    while stack:
        revWords += stack.pop()
        if len(stack) >= 1: revWords += " " 
    return revWords

def allTests():
    assert(reverseWords("") == "")
    assert(reverseWords("hi") == "hi")
    assert(reverseWords("hi there") == "there hi")
    assert(reverseWords("Uber Career Prep") =="Prep Career Uber")
    assert(reverseWords("Emma lives in Brooklyn, New York.") == "York. New Brooklyn, in lives Emma")

allTests()