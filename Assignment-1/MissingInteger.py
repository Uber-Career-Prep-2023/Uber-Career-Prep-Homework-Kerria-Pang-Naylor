"""
Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

Method: Two pointer technique -- fixed sliding window

Time Complexity: O(n) (where n is the size of the array)
Space Complexity: O(1)

Time: 5 minutes
"""
from collections import defaultdict
import math

def solution(arr, n):
    i = 1
    # edge case 1
    if arr[0] != 1:
        return 1
    
    # general case
    while i < len(arr):
        if arr[i] - arr[i-1] > 1:
            return arr[i-1] + 1
        i += 1
    
    # otherwise, missing number is at end
    return n


if __name__ == "__main__":
    # given test cases
    assert solution([1, 2, 3, 4, 6, 7], 7) == 5
    assert solution([1],2) == 2
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12)

    # student test cases
    assert solution([2],2) == 1
    assert solution([1,2,3,4],5) == 5
    assert solution([2,3,3,4],4) == 1


