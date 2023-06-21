"""
Question 8: AlternatingPath
Given an origin and a destination in a directed graph in which edges can be blue or red, determine 
the length of the shortest path from the origin to the destination in which the edges traversed
alternate in color. Return -1 if no such path exists.
"""
from collections import deque, defaultdict
import pdb
# Time Complexity: O(V+E)
# Space Complexity: O(V+E)
# Strategy: BFS
# Time Take: 40 minutes 

def alternatePath(origin, destination, graph:list):
    # create adjacency lists
    adj = defaultdict(lambda: [])
    for start, end, color in graph:
        adj[start].append((end, color))

    # starting at origin, perform BFS on condition that path has to alternate between 
    def bfs_alt(start_node, start_color):
        q = deque()
        visited = set()
        q.appendleft((start_node, start_color, 0)) # last number is degrees outward
        visited.add((start_node, start_color))
        
        while q:
            curr_node, color, deg_out = q.pop()

            # last now looking for opposite color
            if color == "blue": color = "red" 
            else: color = "blue"

            if curr_node[0] == destination:
                return deg_out

            for neighbor, ncolor in adj[curr_node]:
                if ncolor == color and (neighbor, color) not in visited: 
                    q.appendleft((neighbor, ncolor, deg_out + 1))
                    visited.add((neighbor, ncolor))
                    
        return -1
    
    #return bfs_alt(origin)
    blue_len = bfs_alt(origin, "blue") # assume last edge was blue, so first edge is red
    red_len = bfs_alt(origin, "red") # assume last edge was red, so first edge is blue

    if blue_len < 0 and red_len < 0: return -1
    if blue_len < 0: return red_len
    if red_len < 0: return blue_len
    else: return min(blue_len, red_len)


graph = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), 
                        ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), 
                        ("E", "C", "red")]
def testExample1():
    assert(alternatePath("A", "E", graph) == 4)
    assert(alternatePath("E", "D", graph) == -1)
    assert(alternatePath("A", "B", graph) == 1)
    assert(alternatePath("B", "E", graph) == 1)
    assert(alternatePath("B", "C", graph) == 2)

    
testExample1()