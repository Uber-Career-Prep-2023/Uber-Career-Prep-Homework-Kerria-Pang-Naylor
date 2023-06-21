"""
Question 9: MergeKSortedArrays
Given an array of k sorted arrays, merge the k arrays into a single sorted array.
"""
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop

# Time Complexity: O(knlog(n)) where n is the average array length
# Space Complexity: O(kn) because final array combines all elements
# Strategy: Min Heap: First insert first element of all arrays into heap. Pop and add min of heap, 
# insert next element from the array the minimum belonged to.
# Time Take: 40 minutes 


def mergeKSortedArrays(k, arrays:list[list]) -> list:
    # create min-heap of all first elements 
    heap = [(l[0], 0, i) for i, l in enumerate(arrays) if len(l) > 0] # val, index (within array), array index
    heapify(heap)
    sortedL = [] # sorted array 

    # go through every array simultaneously and push on min value to heap, replacing with next el
    while heap:
        min_val, min_i, min_arr_i = heappop(heap) # O(1) operations
        sortedL.append(min_val) 
        
        if (min_i + 1) < len(arrays[min_arr_i]):
            heappush(heap, (arrays[min_arr_i][min_i+1], min_i+1, min_arr_i)) # O(log(n)) operation

    return sortedL

# TESTS
def allTests():
    assert(mergeKSortedArrays(2,[[],[]])==[])
    assert(mergeKSortedArrays(2,[[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]) ==[1, 1, 2, 3, 3, 4, 5, 5, 7, 9])
    assert(mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]])==
           [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16])
    assert(mergeKSortedArrays(3, [[1,2,3], [4,5,6], [7,8,9]])==[1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert(mergeKSortedArrays(3, [[1,2,3], [1,2,3], [1,2,3]])==[1, 1, 1, 2, 2, 2, 3, 3, 3])

allTests()