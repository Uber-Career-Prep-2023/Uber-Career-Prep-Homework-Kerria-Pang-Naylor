"""
Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once. 
If arrays are static (aka, not dynamic/resizable) in your language of choice, the remaining elements should appear in the 
left-hand side of the array and the extra space in the right-hand side should be padded with -1s.

NOTE: Here, I assume we are not allowed to use external data structures (i.e., a hashset) and must modify the array in-place.

Method: Two pointers - variable "sliding window"

Time Complexity: O(n) (where n is the size of the array )
Space Complexity: O(1)

Time: 20 minutes
"""
from collections import defaultdict
import math

def solution(arr):
    last = None
    i_place = 0 # where to place/rewrite next number (stay in place if you want to override something)
 
    for num in arr:
        arr[i_place] = num
        if num != last: # keep in same place if repeat
            i_place += 1
        last = num

    # find index to cut off arr
    i = 1
    while i < len(arr):
        if arr[i-1] >= arr[i]:
            break
        i += 1
        
    return arr[0:i]

                    



if __name__ == "__main__":
    # provided test cases
    assert solution([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 2, 3, 4]
    assert solution([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]) == [0, 1, 4, 5, 8, 9, 10, 11, 15]
    assert solution([1, 3, 4, 8, 10, 12]) == [1, 3, 4, 8, 10, 12]

    # student test cases
    assert solution([]) == []
    assert solution([1, 2, 2, 2, 2, 3]) == [1, 2, 3]
    assert solution([1, 1, 1, 2, 3, 3, 3]) == [1, 2, 3]
    assert solution([1, 2, 2, 9999]) == [1, 2, 9999]