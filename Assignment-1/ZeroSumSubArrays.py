"""
Given an array of integers, count the number of subarrays that sum to zero.

Method: Hashing technique -- One-directional running computation/total


Time Complexity: O(n) (where n is the size of the array)
Space Complexity: O(1)

Time: 35 minutes
"""
from collections import defaultdict
import math

def solution(arr):
    # create running sum as frequency hashmap (find subarray sizes by subtracting indices of prefix sums whose difference is zero)
    sum_ = 0 
    sum_freq = defaultdict(lambda: 0)
    num_zerosubs = 0

    for num in arr:
        sum_ += num
        sum_freq[sum_] += 1

    # if there are more than one occurence of a running sum, there are zero-sum subarray(s)
    for sum_ in sum_freq:
        if sum_freq[sum_] > 1:
            num_zerosubs += math.comb(sum_freq[sum_], 2) # different ways to make substring (so it can handle any all possible subarrays)
        if sum_ == 0:
            num_zerosubs += sum_freq[0] # include prefixes that already sum to zero

    return num_zerosubs

if __name__ == "__main__":
    # given test cases
    assert solution([4, 5, 2, -1, -3, -3, 4, 6, -7]) == 2
    assert solution([1, 8, 7, 3, 11, 9]) == 0
    assert solution([8, -5, 0, -2, 3, -4]) == 2

    # student test cases
    assert solution([]) == 0
    assert solution([0,1,0]) == 2
    assert solution([1,-1]) == 1
    assert solution([0,1,1,-1]) == 2 
    assert solution([0,0,0]) == 6

