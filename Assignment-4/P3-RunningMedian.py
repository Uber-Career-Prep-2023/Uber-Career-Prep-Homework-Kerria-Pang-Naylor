"""
Question 3: RunningMedian
You will be given a stream of numbers, one by one. After each new number, return the median of the numbers so far.

Examples (newest number at each step in bold):
Input: 1
Output: 1

Input: 1, 11
Output: 6

Input: 1, 11, 4
Output: 4

Input: 1, 11, 4, 15
Output: 7.5

Input: 1, 11, 4, 15, 12
Output: 11

NOTE: I used leetcode 295. Find Median from Data Stream environment and template for this problem
"""

# time taken: 30 minutes

# STRATEGY: Multiple Queries --  Two heaps: one min (right heap) and one max (left heap). As you add numbers, keep median. 
# keep track of current median. Input new number into left heap if <=, right heap if >. 
#   If len(right) == len(left), then median == mean of top of both heaps
#   If len(right) > len(left), median = top/min of right heap
#   If len(right) < len(right), median = top/max of left heap

# time complexity : O(nlogn)
# space complexity : O(n)

# This passes all tests on https://leetcode.com/problems/find-median-from-data-stream/submissions/

from heapq import heapify, heappush, heappop # heappush and heappop are log(n)
class MedianFinder:

    def __init__(self):
        self.size = 0
        self.leftMax = [] # max heap on left (all terms negated)
        self.rightMin = [] # min heap on right (insert here if >=)


    def addNum(self, num: int) -> None:
        # even cases
        if len(self.leftMax) == 0 and len(self.rightMin) == 0: # edge case
            heappush(self.rightMin, num)
            return

        if len(self.leftMax) == len(self.rightMin):
            median = float(-1*self.leftMax[0] + self.rightMin[0])/2.0
            if num < median:
                heappush(self.leftMax, -1*num)
            else:
                heappush(self.rightMin, num)
            return

        # odd cases 
        if len(self.leftMax) > len(self.rightMin):
            median = -1*heappop(self.leftMax)

        if len(self.leftMax) < len(self.rightMin):
            median = heappop(self.rightMin)

        if num < median:
            heappush(self.leftMax, -1*num)
            heappush(self.rightMin, median)

        else:
            heappush(self.rightMin, num)
            heappush(self.leftMax, -1*median)


        

    def findMedian(self) -> float:
        if len(self.leftMax) == 0 and len(self.rightMin) == 0: # edge case
            return None

        if len(self.leftMax) == len(self.rightMin):
            return float(-1*self.leftMax[0] + self.rightMin[0])/2.0

        if len(self.leftMax) > len(self.rightMin):
            return -1*self.leftMax[0]

        if len(self.leftMax) < len(self.rightMin):
            return self.rightMin[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

