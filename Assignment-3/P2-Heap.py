"""
Question 2: Build a Heap
Write a min heap class according to the following API using an array as the underlying data
structure. (A max heap has the same implementation; you simply need to flip the direction of the 
comparators.) For simplicity, you can assume that the heap holds integers rather than generic 
comparables.
"""

from math import floor
class Heap:
    def __init__(self) -> None:
        self.arr:int = []

    def top(self) -> int:
        if len(self.arr) > 0:
            return self.arr[0]
    
    # Time Complexity: O(log(n)) (n = size of heap already)
    # Space Complexity: N/A or O(1) (input size can't chance)
    def insert(self, x:int) -> None:
        self.arr.append(x) # put to rightmost bottom child
        i = len(self.arr) - 1

        # bubble up until parent is smaller than it
        parent_i = floor((i - 1)/2)
        while parent_i >= 0 and self.arr[parent_i] > self.arr[i]:
            self.arr[i] = self.arr[parent_i] # swap parent and child
            self.arr[parent_i] = x
            i = parent_i
            parent_i = floor((i - 1)/2)
        
        return
    
    # Time Complexity: O(log(n)) (n = size of heap already)
    # Space Complexity: N/A or O(1) (input size can't chance)
    def delete(self) -> None:
        # move last term to head
        self.arr[0] = self.arr[-1]
        del self.arr[-1]
        
        # swap with smallest children
        i = 0
        childL, childR = i*2 + 1, i*2 + 2

        while childL < len(self.arr) and childR < len(self.arr):
            temp = self.arr[i]
            if self.arr[childL] < self.arr[childR]:
                self.arr[i] = self.arr[childL]
                self.arr[childL] = temp
                i = childL
            else:
                self.arr[i] = self.arr[childR]
                self.arr[childR] = temp
                i = childR
            
            childL, childR = i*2 + 1, i*2 + 2 # update child indices

        # catch case where you must delete with one child out of rance
        if childL >= len(self.arr) and childR < len(self.arr) and self.arr[childR] < self.arr[i]: 
            temp = self.arr[childR] 
            self.arr[childR] = self.arr[i]
            self.arr[i] = temp
        if childR >= len(self.arr) and childL < len(self.arr) and self.arr[childL] < self.arr[i]: 
            temp = self.arr[childL] 
            self.arr[childL] = self.arr[i]
            self.arr[i] = temp

    def returnArr(self) -> list: # for testing
        return self.arr

        


    
# tests
def testAll():
    a = Heap()
    a.insert(3)
    assert(a.returnArr() == [3])
    assert(a.top() == 3)

    a.insert(4)
    assert(a.returnArr() == [3, 4])
    assert(a.top() == 3)

    a.insert(1)
    assert(a.returnArr() == [1,4,3])
    assert(a.top() == 1)

    a.insert(0)
    assert(a.returnArr() == [0,1,3,4])
    assert(a.top() == 0)
    
    a.delete()
    assert(a.returnArr() == [1,4,3])
    
    a.delete()
    assert(a.returnArr() == [3,4])

    a.delete()
    assert(a.returnArr() == [4])

    a.delete()
    assert(a.returnArr() == [])



testAll()
