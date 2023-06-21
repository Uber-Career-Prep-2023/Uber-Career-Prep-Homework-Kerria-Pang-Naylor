"""
Question 11: VacationDestinations
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached 
directly from each other with corresponding travel times in hours, return the number of 
destinations within k hours of the origin. Assume that having a stopover in a city adds an hour of
travel time.
"""
from collections import deque, defaultdict
import pdb

# Time Complexity: O(V+O)
# Space Complexity: O(V)
# Strategy: BFS
# Time Taken: 15 minutes 

def vacationDestinations(origin, k, edges):
    # create adjacency list
    neighbors = defaultdict(lambda: [])
    for start, end, weight in edges:
        neighbors[start].append((end, weight))
        neighbors[end].append((start,weight))
    cities = []
    ncities = 0

    # perform BFS and keep track of time "distance"
    visited = set()
    q = deque()
    q.appendleft((origin, -1)) # queue stores city and distance from origin, origin is -1 because no wait time for start location
    visited.add(origin)
    while q:
        city, distance = q.pop()
        if distance < k:
            ncities += 1
            cities.append(city)
            for ncity, ndistance in neighbors[city]:
                if ncity not in visited: 
                    q.appendleft((ncity, ndistance +1+ distance)) # append (cityname, new distance + 1 (wait time))
                    visited.add(ncity)
        elif distance == k: # if reached maximum time, append city and no more search
            ncities += 1
            cities.append(city)
        else:
            pass
    return ncities - 1, cities[1:] # exclude origin city

def exampleTests():
    edges =  [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
    assert(vacationDestinations("New York", 5, edges)== (2, ['Boston', 'Philadelphia']))
    assert(vacationDestinations("New York", 7, edges)==(4, ['Boston', 'Philadelphia', 'Newport', 'Washington, D.C.']))
    assert(vacationDestinations("New York", 8, edges)==(6, ['Boston', 'Philadelphia', 'Newport', 'Portland', 'Washington, D.C.', "Harper's Ferry"]))

def basicTests():
    edges = [("a", "b", 1), ("b", "c", 2), ("b", "d", 4)]
    assert(vacationDestinations("a",1, edges) == (1, ["b"]))
    assert(vacationDestinations("a",3, edges) == (1, ["b"]))
    assert(vacationDestinations("a",4, edges) == (2, ["b", "c"]))
    assert(vacationDestinations("a",9, edges) == (3, ["b", "c", "d"]))
    assert(vacationDestinations("a",10, edges) == (3, ["b", "c", "d"]))

exampleTests()
basicTests()