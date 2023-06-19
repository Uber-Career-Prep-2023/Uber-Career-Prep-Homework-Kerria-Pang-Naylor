"""
Question 4: NumberOfIslands
Given a binary matrix in which 1s represent land and 0s represent water. Return the number of      
islands (contiguous 1s surrounded by 0s or the edge of the matrix).
"""
from collections import deque
import pdb
# Strategy: Generic Graph Traversal-- Breadth-first Search
# Time Complexity: O(n) (n is cells in matrix)
# Space Complexity: O(n)
# Time: 45 minutes

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # algorithm: search through every cell. If "1" and marked unvisited, perform BFS on only 
    # adjacent "1" cells to mark all cells in island as visited.
    if grid == []: return 0
    
    visited = set()
    def bfs(x_start, y_start):
        q = deque()
        q.appendleft((x_start,y_start))
        visited.add((x_start,y_start))
        while q:
            x,y = q.pop()
            neighbors = [(x+a[0], y+a[1]) for a in [(1,0), (0,1), (-1, 0), (0, -1)] if x+a[0] in range(len(grid)) and y+a[1] in range(len(grid[0]))]
        
            for xn, yn in neighbors:
                if (xn,yn) not in visited and grid[xn][yn] == 1: 
                    visited.add((xn,yn))
                    q.appendleft((xn, yn))
        

    num = 0 # num islands
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):

            if (x,y) not in visited and grid[x][y] == 1:
                bfs(x, y) # mark whole island as visited
                num += 1
    
    return num



def allTests():
    assert(numIslands([]) == 0)
    assert(numIslands([[1,0,1,1,1],[1,1,0,1,1],[0,1,0,0,0], [0,0,0,1,0],[0,0,0,0,0]]) == 3)
    assert(numIslands([[1,1,1], [1,1,1], [1,1,1], [1,1,1]]) == 1)
    assert(numIslands([[0,0,0], [1,0,0]]) == 1)
    assert(numIslands([[0,1,0],[1,0,1],[0,1,0]]) == 4)
    
allTests()