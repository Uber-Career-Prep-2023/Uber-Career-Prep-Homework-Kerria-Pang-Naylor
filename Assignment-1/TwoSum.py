"""
Given an array of integers and a target integer, k, return the number of pairs of integers in the array that sum to k.
In each pair, the two items must be distinct elements (come from different indices in the array).

Method: One-directional running computation/total


Time Complexity: O(n) (where n is the size of the array )
Space Complexity: O(n)

Time: 25 minutes
"""
from collections import defaultdict
import math

def solution(arr, k):
    num_pairs = 0
    past = defaultdict(lambda: 0) # maps vals to num occurences

    for val in arr:
        if k - val in past: # find past value in map that adds to target
            num_pairs += past[k - val]
        past[val] += 1

    return num_pairs



if __name__ == "__main__":
    # given test cases
    assert solution([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10) == 3
    assert solution( [1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 9) == 4
    assert solution([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6) == 5
    assert solution([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1) == 0

    # student test cases
    assert solution([], 10) == 0
    assert solution([1,1,3,1], 4) == 3
    assert solution([2,-100,102,0], 2) == 2
