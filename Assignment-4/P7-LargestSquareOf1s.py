"""
Question 7: LargestSquareOf1s
Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.
https://leetcode.com/problems/maximal-square/
"""

# Strategy: recursion + memoization
# Brute force strategy: go through every point and find largest square where upper left corner is that point 
# Recursive idea: for any point = 1, it is the lower right corner of a square with side length = 1+ the minimum of the 
# side lengths of the squares ending at the points directly above, left, and diagonally up/left

# Time complexity: O(m*n)
# Space complexity: O(m*n)

# Time taken: ~20 minutes
def maximalSquare( matrix: list[list[str]]) -> int:
    # stores largest square length ending at certain point
    memo = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]

    def largestSquareAt(row,col): # returns largest square length whose lower right corner is row col   
        if matrix[row][col] == "0": # only consider when valid endpoint
            return 0
        # base case, if on left or upper wall, maximum square side length == 1 
        if memo[row][col]:
            return memo[row][col] 
        if row == 0 or col == 0:
            memo[row][col] = 1
            return 1
        
        # recursive case
        ret = 1+ min(largestSquareAt(row-1, col), largestSquareAt(row-1, col-1), largestSquareAt(row,col-1))
        memo[row][col] = ret
        return ret
    largest_length = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            largest_length = max(largest_length, largestSquareAt(row,col))
    
    return largest_length#**2 for leetcode where you return area

"""
------------------------------
            TESTS
------------------------------
"""
# NOTE: this solution passes all test cases on https://leetcode.com/problems/maximal-square/description/

def tests():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert(maximalSquare(matrix) == 2)

    matrix = [["0","1"],["1","0"]]
    assert(maximalSquare(matrix) == 1)

    matrix = [["0"]]
    assert(maximalSquare(matrix)==0)

tests()