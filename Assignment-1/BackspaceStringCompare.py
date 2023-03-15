"""
Given two strings representing series of keystrokes, determine whether the resulting text is the same. 
Backspaces are represented by the '#' character so "x#" results in the empty string ("").

Method: Two-pointers -- simultaneous two arrays/strings two-pointer

Time Complexity: O(n) (where n is the size of the array)
Space Complexity: O(1)

Time: 20 minutes
"""
from collections import deque

# optimal solution with simultaneous two pointers on two strings (grade this) -- better than stack solution because O(1) space complexity
def solution(s1, s2):
    r1 = len(s1) - 1
    r2 = len(s2) - 1
    backs1 = 0 # num backspaces/things to skip
    backs2 = 0 

    # two pointers starting on right side, to left
    while r1 > 0 and r2 > 0:
        if s1[r1] == '#' or s2[r2] == '#': # tally up backspaces
            if s1[r1] == '#':
                backs1 += 1
                r1 -= 1
            if s2[r2] == '#':
                backs2 += 1
                r2 -= 1
            continue
        
        if backs1 == 0 and backs2 == 0:
            if s1[r1] != s2[r2]:
                return False
            r1 -= 1
            r2 -= 1
        else:
            # if you have backspaces tallied, skip over next letters
            if backs1 > 0:
                r1 -= 1
                backs1 -= 1
            if backs2 > 0:
                r2 -= 1
                backs2 -= 1
    return True

                        


# Non-optimal stack solution (because it would take O(n) space complexity), treats strings starting with backspace as invalid input
def solution_stack(s1, s2):

    # correct s1 and s2 for backspaces
    new_s1 = deque()
    new_s2 = deque()

    # one pass, push letters, pop when you see '#'
    for char in s2:
        if char == "#":
            new_s2.pop()
        else:
            new_s2.append(char)

    for char in s1:
        if char == "#":
            new_s1.pop()
        else:
            new_s1.append(char)
    

    # check each queue
    if len(new_s1) != len(new_s2):
        return False 
    
    while len(new_s2) > 0:
        last1 = new_s1.pop()
        last2 = new_s2.pop()

        if last1 != last2:
            return False
    
    return True



if __name__ == "__main__":
    # provided test cases
    assert solution("abcde", "abcde")
    assert solution("Uber Career Prep", "u#Uber Careee#r Prep")
    assert solution("abcdef###xyz", "abcw#xyz")
    assert solution("abcdef###xyz", "abcdefxyz###") == False

    # student test cases
    assert solution("", "")
    assert solution("abcdefg#######", "")
    assert solution("###potato", "potatoo#")
    assert solution("########", "")