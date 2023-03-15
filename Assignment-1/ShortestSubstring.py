"""
Given a string and a second string representing required characters, return the length of the shortest
substring containing all the required characters.

Method: Two pointer technique -- Variable-size (shrinking/growing) sliding window

Time Complexity: O(n) (where n is the size of the array )
Space Complexity: O(1)

Time: 40 minutes
"""
from collections import defaultdict
import math
def solution(s1, s2):
    sstr_lens = [] # valid substring lengths
    freq = defaultdict(lambda: 0) # frequency dict needs all numbers >= 0 to be valid substring
   
    for char in s2:
        freq[char] -= 1

    l = 0
    r = 0

    if s1[r] in freq:
        freq[s1[r]] += 1

    while l < len(s1) and r < len(s1):
        # print(freq)
        if valid_d(freq):
            sstr_lens.append(r - l + 1)
            if s1[l] in freq:
                freq[s1[l]] -= 1
            l += 1

        else:
            r += 1
            if r < len(s1) and s1[r] in freq:
                freq[s1[r]] += 1
                
    
    return min(sstr_lens)

def valid_d(d): # does the substring have everything you need
    for char in d:
        if d[char] < 0:
            return False
    return True


if __name__ == "__main__":
    # given test cases
    assert solution("abracadabra", "abc") == 4
    assert solution("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx") == 10
    assert solution("dog", "god") == 3

    # student test cases
    assert solution("a", "a") == 1 
    assert solution("caaaaaaaat", "cat") == 10
    assert solution("caaaaaaaatxxxxcatxx", "cat") == 3
    assert solution("caaaaaaaatxxxxtacxx", "cat") == 3
