"""
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k characters in one of the strings. 
Given two strings and an integer k, determine if they are k-anagrams.

Method: Hashing technique -- Variable-size (shrinking/growing) sliding window

Time Complexity: O(n) 
Space Complexity: O(n)

Time: 15 minutes
"""
from collections import defaultdict


def solution(s1, s2, k):
    # eliminate if not same length
    if len(s1) != len(s2):
        return False
    # first get frequency hashmaps of strings (include characters in one but not the other)
    count1 = defaultdict(lambda: 0)
    count2 = defaultdict(lambda: 0)

    for char in s1:
        count1[char] += 1
        count2[char] = 0
    
    for char in s2:
        count2[char] += 1
        if char not in count1:
            count1[char] = 0

    # count number of needed changes to turn s1 into s2
    num_differences = 0

    for char in count1:
        num_differences += abs(count1[char] - count2[char])
    
    return num_differences/2 <= k # divide by two because two differences in frequency is one letter flip


if __name__ == "__main__":
    # provided test cases
    assert solution("apple", "peach", 1) == False
    assert solution("apple", "peach", 2)
    assert solution("cat", "dog", 3)
    assert solution("debit curd", "bad credit", 1)
    assert solution("baseball", "basketball", 2) == False

    # student test cases
    assert solution("", "", 1)
    assert solution("potato", "potatooo", 500) == False
    assert solution("cheese", "cheese", 0) 
    assert solution("parmesan", "parmesai", 1)
