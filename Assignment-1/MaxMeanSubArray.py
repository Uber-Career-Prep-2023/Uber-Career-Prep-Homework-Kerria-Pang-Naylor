"""
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Method: Two pointer technique -- fixed-size sliding window

Time Complexity: O(n) (where n is the size of the array )
Space Complexity: O(1)

Time: 20 minutes
"""

def solution(arr, k):
    l = 0
    r = k # right pointer is one past last index we're considering
    sum_ = sum(arr[0:r]) # running sum 
    max_mean = sum_/k # running maximum sum  


    while r < len(arr):
        sum_ += arr[r] # move window/update sum
        sum_ -= arr[l]
        
        if sum_/k > max_mean: # update mean
            max_mean = sum_/k

        l+=1 # move indices
        r+=1 

    return max_mean


if __name__ == "__main__":
    # Provided test cases
    arr = [4, 5, -3, 2, 6, 1]
    k = 2
    assert solution(arr, k) == 4.5

    arr = [4, 5, -3, 2, 6, 1]
    k = 3
    assert solution(arr, k) == 3

    arr = [1, 1, 1, 1, -1, -1, 2, -1, -1]
    k = 3
    assert solution(arr, k) == 1

    arr = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
    k = 5
    assert solution(arr, k) == 1
    
    # Student test cases

    