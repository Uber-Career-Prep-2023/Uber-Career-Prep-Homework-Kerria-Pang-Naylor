"""
Question 1: Build an Adjacency List/Set Representation of a Graph

Given an array of pairs of values representing edges in an unweighted graph, create the equivalent
adjacency list/set representation (a map from element to a list or set of elements). Pairs 
represent directed edges: (A, B) means there is an edge from A to B. If the pair (B, A) is also 
provided then there is an undirected edge between A and B. For simplicity, you may assume that each 
node of the graph stores an integer rather than a generic data type and that the elements are 
distinct. Implement a basic DFS and BFS searching for a target value and a topological sort (using 
either DFS or Kahn’s algorithm).
"""
from collections import defaultdict
from collections import deque
import pdb

# adjacencySet
# Time Complexity : O(n)
# Space Complexity : O(n)
def adjacencySet(pairs:list) -> dict:
    adj_list = defaultdict(lambda: set()) # if key doesn't exist, will make key
    
    for pair in pairs:
        adj_list[pair[0]].add(pair[1])
        if pair[1] not in adj_list: adj_list[pair[1]] # if node as no out edges

    return dict(adj_list)


# BFS
# Time Complexity : O(n) (since I keep track of formerly visited nodes)
# Space Complexity : O(n)
# NOTE: I am accounting for the case where we might have a disconnected digraph and/or dead ends,
# so this is a bit more complicated than the classic undirected, connected graph bfs
def bfs(target:int, graph:dict) -> bool:
    visited = set() # set of visited nodes (integers), held throughout all bfs searches

    def bfs_start(start_node:int) -> bool:  # helper simple bfs given start
        queue = deque()
        queue.appendleft(start_node)
        visited.add(start_node)

        while queue:
            curr_node = queue.pop()
            if curr_node == target: return True

            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.appendleft(neighbor)
        return False
    
    for node in graph: # every possible starting node so it works with disconnected graphs
        if node not in visited: # prevent repeat searches -- algorithm will only visit each node once
            if bfs_start(node): return True
    
    return False


# DFS with iterative (stack-based) helper
# Time Complexity : O(n^2) for version without start given, O(n) when start node is given
# Space Complexity : O(1)
def dfs(target, graph:dict) -> bool:
    visited = set() # set of visited nodes (integers)

    def dfs_start(start_node:int) -> bool:  # helper simple dfs given start
        stk = deque()
        stk.append(start_node)
        visited.add(start_node)

        while stk:
            curr_node = stk.pop()
            if curr_node == target: return True
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stk.append(neighbor)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs_start(node): return True

    return False # if searched through entire graph without finding target, target isn't here

# recursive version of dfs_start
def dfs_rec(target, graph:dict, start_node, visited:set = set()) -> bool:
    visited.add(start_node)

    for neighbor in graph[start_node]: # go through neigbors
        dfs_rec(target, graph, neighbor, visited)




# Topological Sort -- DFS Algorithm
# Time Complexity : O(n)
# Space Complexity : O(n)
def topologicalSort(graph:dict) -> list:
    
    visited = [False]*len(graph) # set of visited nodes (integers), could also use list
    sorted = deque()

    def dfs_rec(start_node) -> bool:
        visited[start_node] = True

        for neighbor in graph[start_node]: # go through neigbors
            if not visited[neighbor]: dfs_rec(neighbor)
        
        sorted.appendleft(start_node)
    
    for node in graph:
        if not visited[node]:
            dfs_rec(node)

    return list(sorted) # if searched through entire graph without finding target, target isn't here

    




# Topological Sort -- Kahn's algorithm
# Time Complexity : O(n) (vertices + edges)
# Space Complexity : O(1)
def topologicalSort_Kahn(graph:dict) -> list:
    sorted = deque()
    # initialize in-degree tracker array
    in_degrees = [0]*len(graph)
    for node in range(len(in_degrees)):
        for neighbor in graph[node]:
            in_degrees[neighbor] += 1

    # initialize queue for set of nodes with zero in-edges
    queue = deque()
    for node in range(len(in_degrees)):
        if in_degrees[node] == 0:
            queue.appendleft(node)

    # put node from queue onto sorted, update in-degrees
    while queue:
        curr_node = queue.pop()
        sorted.append(curr_node)
        for neighbor in graph[curr_node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0: queue.appendleft(neighbor)


    return list(sorted)



# TESTS -- adjacencySet
def emptyTest_adjacencySet():
    assert(adjacencySet([]) == {})

def nodeTest_adjacencySet():
    assert(adjacencySet([(0,1)]) == {0: {1}, 1: set()})
    
def exampleTest_adjacencySet():
    assert(adjacencySet([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]) == 
           {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}})

def stickTest_adjacencySet():
    assert(adjacencySet([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]) == 
           {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()})
    
def circleTest_adjacencySet():
    assert(adjacencySet([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]) == 
           {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}})

emptyTest_adjacencySet()
nodeTest_adjacencySet()
exampleTest_adjacencySet()
stickTest_adjacencySet()
circleTest_adjacencySet()

# TESTS -- bfs
def emptyTest_bfs():
    assert(not bfs(0, {}))
    assert(not bfs(99, {}))

def nodeTest_bfs():
    assert(bfs(0, {0: {1}, 1: set()}))
    assert(bfs(1, {0: {1}, 1: set()}))
    assert(not bfs(2, {0: {1}, 1: set()}))
    
def exampleTest_bfs():
    assert(bfs(0, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(bfs(1, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(bfs(2, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(bfs(3, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(not bfs(5, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))

def stickTest_bfs():
    assert(bfs(0, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(bfs(1, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(bfs(2, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(bfs(3, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(bfs(4, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(bfs(5, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(not bfs(9999, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))

    
def circleTest_bfs():
    assert(bfs(0, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(bfs(1, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(bfs(2, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(bfs(3, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(bfs(4, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(bfs(5, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(not bfs(6, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))

def disconnectedTest_bfs():
    assert(bfs(0, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(bfs(1, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(bfs(2, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(bfs(3, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(not bfs(4, {0: {1}, 1: {0}, 2: {3}, 3: set()}))


emptyTest_bfs()
nodeTest_bfs()
exampleTest_bfs()
stickTest_bfs()
circleTest_bfs()
disconnectedTest_bfs()

# TESTS -- dfs
def emptyTest_dfs():
    assert(not dfs(0, {}))
    assert(not dfs(99, {}))

def nodeTest_dfs():
    assert(dfs(0, {0: {1}, 1: set()}))
    assert(dfs(1, {0: {1}, 1: set()}))
    assert(not dfs(2, {0: {1}, 1: set()}))
    
def exampleTest_dfs():
    assert(dfs(0, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(dfs(1, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(dfs(2, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(dfs(3, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))
    assert(not dfs(5, {0: set(), 1: {2, 3}, 2: {0, 3}, 3: {2}}))

def stickTest_dfs():
    assert(dfs(0, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(dfs(1, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(dfs(2, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(dfs(3, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(dfs(4, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(dfs(5, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))
    assert(not dfs(9999, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: set()}))

    
def circleTest_dfs():
    assert(dfs(0, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(dfs(1, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(dfs(2, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(dfs(3, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(dfs(4, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(dfs(5, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))
    assert(not dfs(6, {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {0}}))

def disconnectedTest_dfs():
    assert(dfs(0, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(dfs(1, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(dfs(2, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(dfs(3, {0: {1}, 1: {0}, 2: {3}, 3: set()}))
    assert(not dfs(4, {0: {1}, 1: {0}, 2: {3}, 3: set()}))


emptyTest_dfs()
nodeTest_dfs()
exampleTest_dfs()
stickTest_dfs()
circleTest_dfs()
disconnectedTest_dfs()

# TESTS -- topologicalSort (DFS)
def emptyTest_topSort():
    assert(topologicalSort({}) == [])

def oneNodeTest_topSort():
    assert(topologicalSort({0: set()}) == [0])

def threeNodeTest_topSort():
    assert(topologicalSort({0: set(), 1: set(), 2: {0, 1}}) == [2, 1, 0])

def fourNodeTest_topSort():
    assert(topologicalSort({0: set(), 1: set(), 2: {0, 1}, 3: {0, 1, 2}}) == [3, 2, 1, 0])

def sixNodeTest_topSort():
    assert(topologicalSort({0: set(), 1: set(), 2: {3}, 3: {1}, 4: {0,1}, 5: {0,2}}) == [5, 4, 2, 3, 1, 0])

def stickTest_topSort():
    assert(topologicalSort({0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: set()}) == [0, 1, 2, 3, 4])

emptyTest_topSort()
oneNodeTest_topSort()
fourNodeTest_topSort()
sixNodeTest_topSort()
stickTest_topSort()

# TESTS -- topologicalSort (Kahn's)
def emptyTest_topSort_Kahn():
    assert(topologicalSort_Kahn({}) == [])

def oneNodeTest_topSort_Kahn():
    assert(topologicalSort_Kahn({0: set()}) == [0])

def threeNodeTest_topSort_Kahn():
    assert(topologicalSort_Kahn({0: set(), 1: set(), 2: {0, 1}}) == [2, 1, 0])

def fourNodeTest_topSort_Kahn():
    assert(topologicalSort_Kahn({0: set(), 1: set(), 2: {0, 1}, 3: {0, 1, 2}}) == [3, 2, 0, 1])

def sixNodeTest_topSort_Kahn():
    assert(topologicalSort_Kahn({0: set(), 1: set(), 2: {3}, 3: {1}, 4: {0,1}, 5: {0,2}}) == [4, 5, 0, 2, 3, 1])

def stickTest_topSort_Kahn():
    assert(topologicalSort_Kahn({0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: set()}) == [0, 1, 2, 3, 4])

emptyTest_topSort_Kahn()
oneNodeTest_topSort_Kahn()
fourNodeTest_topSort_Kahn()
sixNodeTest_topSort_Kahn()
stickTest_topSort_Kahn()