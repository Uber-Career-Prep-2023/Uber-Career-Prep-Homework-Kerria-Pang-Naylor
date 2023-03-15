"""
Given a list of integer pairs representing the low and high end of an interval, inclusive, 
return a list in which overlapping intervals are merged.

Method: Sort the array, then solve

Time Complexity: O(nlogn) (where n is the size of the array )
Space Complexity: O(n)

Time: 25 minutes
"""
from collections import defaultdict
import math

def solution(arr):
    ret = [] # return/overlapping intervals
    # sort array by lower ranges O(nlogn)
    arr = sorted(arr)

    # use sorted array to get ranges
    l = 0
    r = 0

    while r < len(arr):
        curr_min = arr[l][0]
        curr_max = arr[l][1]

        # attach overlapping tuples together O(n)
        while r < len(arr) and curr_max >= arr[r][0]:
            curr_min = min(curr_min, arr[r][0])
            curr_max = max(curr_max, arr[r][1])
            r+=1
            
        ret.append((curr_min, curr_max))
        l = r
        if r < len(arr):
            curr_min, curr_max = arr[l][0], arr[l][1]
    return ret



    



if __name__ == "__main__":
    # given test cases
    assert solution([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]) == [(1, 3), (4, 8), (9, 12)]
    assert solution([(5, 8), (6, 10), (2, 4), (3, 6)]) == [(2,10)]
    assert solution([(10, 12), (5, 6), (7, 9), (1, 3)]) == [(1, 3), (5, 6), (7, 9), (10, 12)]

    # student test cases
    assert solution([]) ==[]
    assert solution([(1,100), (2,3), (3,9), (6,10)]) ==[(1,100)]
    assert solution([(1,2), (4,5), (5,6)]) == [(1,2), (4,6)]
    assert solution ([(99,100), (0,5), (2,3)]) == [(0,5), (99,100)]