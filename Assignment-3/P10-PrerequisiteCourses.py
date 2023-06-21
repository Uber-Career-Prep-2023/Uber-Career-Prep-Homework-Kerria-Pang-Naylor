"""
Question 10: PrerequisiteCourses
Given a list of courses that a student needs to take to complete their major and a map of courses 
to their prerequisites, return a valid order for them to take their courses assuming they only 
take one course for their major at once.
"""

from collections import deque, defaultdict
import pdb

# Time Complexity: O(V+O)
# Space Complexity: O(V)
# Strategy: Topological Sort (DFS)
# Time Taken: 15 minutes 

def prereqCourses(courses, adj):
    visited = set() # all visited courses
    sorted = deque() # stack for sorted courses

    def dfs(start_node):
        visited.add(start_node)
        if start_node in adj: 
            for neighbor in adj[start_node]:
                if neighbor in visited: dfs(neighbor)
        sorted.appendleft(start_node)
    
    for course in courses:
        if course not in visited:  dfs(course)
    
    return list(sorted)

def exampleTests():
    res = prereqCourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] })
    assert(res == ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"] or 
        ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"])
    
    res = prereqCourses(["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] })
    assert(res == ["Intro to Writing", "Plays & Screenplays", "Contemporary Literature", "Ancient Literature", "Comparative Literature"] or
        ["Intro to Writing", "Contemporary Literature", "Plays & Screenplays", "Ancient Literature", "Comparative Literature"] or
        ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Plays & Screenplays", "Comparative Literature"] or 
        ["Intro to Writing", "Ancient Literature", "Contemporary Literature",  "Plays & Screenplays", "Comparative Literature"] or 
        ["Intro to Writing", "Ancient Literature",  "Plays & Screenplays",  "Contemporary Literature", "Comparative Literature"] or
        ["Intro to Writing", "Plays & Screenplays", "Ancient Literature",  "Contemporary Literature", "Comparative Literature"] or 
        ["Intro to Writing", "Ancient Literature",  "Contemporary Literature", "Comparative Literature", "Plays & Screenplays"] or 
        ["Intro to Writing", "Contemporary Literature",  "Ancient Literature", "Comparative Literature", "Plays & Screenplays"] )

def basicTests():
    res = prereqCourses([], {})
    assert(res == [])

    res = prereqCourses(["a", "b"], {"a":["b"]})
    assert(res == ["a", "b"])

    res = prereqCourses(["a", "b", "c"], {"a": ["b"], "b":["c"]})
    assert(res == ["a", "b", "c"])

exampleTests()