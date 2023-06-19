"""
Question 6: RoadNetworks
In some states, it is not possible to drive between any two towns because they are not connected 
to the same road network. Given a list of towns and a list of pairs representing roads between 
towns, return the number of road networks. (For example, a state in which all towns are connected 
by roads has 1 road network, and a state in which none of the towns are connected by roads has 0 
road networks.)
"""

# Strategy: generic traversal with breadth-first search
# Time Complexity: O(V+E) -- only doing full computation for each number once because of memoization
# Space Complexity: O(V+E) -- due to memoization
# Time: 30 minutes

# assuming that you can drive on both sides or the road, this is an undirected graph
from collections import defaultdict, deque
def roadNetworks(towns:list, roads:list):
    
    # first make adjacency list so we don't have to perform search every time (O(V+E))
    neighbors = defaultdict(lambda: [])
    for road in roads:
        neighbors[road[0]].append(road[1])
        neighbors[road[1]].append(road[0])
    print(neighbors)

    # go through every town and perform BFS to visit all accessible towns (O(V+E))
    visited = set() # visited towns
    networks = 0

    def bfs(town):
        #pdb.set_trace()
        q = deque()
        q.appendleft(town)
        visited.add(town)

        while q:
            curr_town = q.pop()
            for neighbor in neighbors[curr_town]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.appendleft(neighbor)
        return 


    for town in towns:
        if town not in neighbors: continue # means town is has no paths to anything, is not a part of network
        if town not in visited:
            bfs(town)
            networks += 1

    return networks

def testExample():
    towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"]
    connections = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    assert(roadNetworks(towns, connections) == 2)

def testExample2():
    towns = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    connections = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"),("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    assert(roadNetworks(towns, connections) == 3)

testExample()
testExample2()