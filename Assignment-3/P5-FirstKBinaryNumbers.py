"""
Question 5: FirstKBinaryNumbers
Given a number, k, return an array of the first k binary numbers, represented as strings.
"""
# Strategy: memoization/hashmap + recursion
# Time Complexity: O(n) -- only doing full computation for each number once because of memoization
# Space Complexity: O(n) -- due to memoization
# Time: 20 minutes
def decToBin(n, memo): # recursive helper, converts decimal to binary string
    if n == 0: return ""
    if n in memo: return memo[n]
    elif n%2 == 0:
        soln = decToBin(n/2, memo)+"0"
        memo[n] = soln
        return soln
    else:
        soln = decToBin((n-1)/2, memo) + "1"
        memo[n] = soln
        return soln

def firstKBinaryNumbers(k): 
    if k < 0:
        raise Exception("k must be a non-negative integer")
    memo = {} # maps number to binary string rep
    ret = ["0"] # assume k >= 0
    for n in range(1,k):
        print(memo)
        ret.append(decToBin(n, memo))
    return ret


# TESTS

def allTests():
    assert(firstKBinaryNumbers(0) == ["0"])
    assert(firstKBinaryNumbers(1) == ["0"]) 
    assert(firstKBinaryNumbers(5) == ["0", "1", "10", "11", "100"])
    assert(firstKBinaryNumbers(10) == ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
)

allTests()