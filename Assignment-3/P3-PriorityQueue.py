"""
Question 3: Build a Priority Queue
A priority queue functions like a queue except that elements are removed in order of priority 
rather than insertion. This is typically implemented as a max heap that stores pairs of elements 
and numeric weights, with the weights used as the values in the heap. Implement a priority queue 
according to the following API using a heap as the underlying data structure. For simplicity, you 
can assume the priority queue stores string elements with integer priorities. Start by copy-pasting 
your heap implementation from question 2 and making modifications.
"""

from math import floor
class PriorityQueue:
    def __init__(self) -> None:
        self.arr = [] # consists of (str, int), sorted by int

    def top(self):
        if len(self.arr) > 0:
            return self.arr[0]
    
    # Time Complexity: O(log(n)) (n = size of heap already)
    # Space Complexity: N/A or O(1) (input size can't chance)
    def insert(self, x:str, weight:int) -> None:
        self.arr.append((x,weight)) # put to rightmost bottom child
        i = len(self.arr) - 1

        # bubble up until parent is larger than it
        parent_i = floor((i - 1)/2)
        while parent_i >= 0 and self.arr[parent_i][1] < self.arr[i][1]:
            self.arr[i] = self.arr[parent_i] # swap parent and child
            self.arr[parent_i] = (x, weight)
            i = parent_i
            parent_i = floor((i - 1)/2)
        
        return
    
    # Time Complexity: O(log(n)) (n = size of heap already)
    # Space Complexity: N/A or O(1) (input size can't chance)
    def delete(self) -> None:
        # move last term to head
        self.arr[0] = self.arr[-1]
        del self.arr[-1]
        
        # swap with largest children
        i = 0
        childL, childR = i*2 + 1, i*2 + 2

        while childL < len(self.arr) and childR < len(self.arr):
            temp = self.arr[i]
            if self.arr[childL][1] > self.arr[childR][1]:
                self.arr[i] = self.arr[childL]
                self.arr[childL] = temp
                i = childL
            else:
                self.arr[i] = self.arr[childR]
                self.arr[childR] = temp
                i = childR
            
            childL, childR = i*2 + 1, i*2 + 2 # update child indices

        # catch case where you must delete with one child out of rance
        if childL >= len(self.arr) and childR < len(self.arr) and self.arr[childR][1] > self.arr[i][1]: 
            temp = self.arr[childR] 
            self.arr[childR] = self.arr[i]
            self.arr[i] = temp
        if childR >= len(self.arr) and childL < len(self.arr) and self.arr[childL][1] > self.arr[i][1]: 
            temp = self.arr[childL] 
            self.arr[childL] = self.arr[i]
            self.arr[i] = temp
        return
    
    def returnArr(self) -> list: # for testing
        return self.arr

        


    
# tests
def testAll():
    a = PriorityQueue()
    a.insert("c", 3)
    assert(a.returnArr() == [("c", 3)])
    assert(a.top() == ("c", 3))

    a.insert("d", 4)
    assert(a.returnArr() == [("d", 4), ("c", 3)])
    assert(a.top() == ("d", 4))

    a.insert("a", 1)
    assert(a.returnArr() == [("d", 4), ("c", 3), ("a", 1)])
    assert(a.top() == ("d", 4))

    a.insert("b", 2)
    assert(a.returnArr() == [("d", 4), ("c", 3), ("a", 1), ("b", 2)])
    assert(a.top() == ("d", 4))

    a.insert("e", 5)
    assert(a.returnArr() == [("e", 5), ("d", 4), ("a", 1), ("b", 2), ("c", 3)])
    assert(a.top() == ("e", 5))
    
    a.delete()
    assert(a.returnArr() == [("d", 4), ("c", 3), ("a", 1), ("b", 2)])
    
    a.delete()
    assert(a.returnArr() == [("c", 3), ("b", 2), ("a", 1)])

    a.delete()
    assert(a.returnArr() == [("b", 2), ("a", 1)])

    a.delete()
    assert(a.returnArr() == [("a", 1)])

    a.delete()
    assert(a.returnArr() == [])

testAll()