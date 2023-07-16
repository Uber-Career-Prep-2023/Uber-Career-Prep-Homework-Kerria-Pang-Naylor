"""
Question 4: Catalan Numbers
The Catalan numbers are a mathematical sequence of numbers. The nth Catalan number is defined as 
(2n)! / (n+1)!n!. Given a non-negative integer n, return the Catalan numbers 0-n.
"""

# Time complexity:  O(n)
# Space comoplexity: O(n)

# time taken: 20 minutes

# STRATEGY: Dynamic Programming -- Memoization/save partial results

def catalanNumbers(n:int) -> list[int]:
    memo = {} # stores all factorials

    def fac(n:int) -> int:
        if n == 0:
            return 1
        if n in memo:
            return memo[n]
        ret = n*fac(n-1)
        memo[n] = ret
        return ret
    
    def getNumber(n):
        return fac(2*n)/(fac(n+1)*fac(n))

    
    numbers = []
    for i in range(2*n): # build all needed factorials in memo, O(n) w/ DP/memoization
        fac(i)
    
    for i in range(n+1): # build returns, O(n)
        numbers.append(getNumber(i))
    return numbers


"""
------------------------------
            TESTS
------------------------------
"""

def test1():
    assert(catalanNumbers(1) == [1,1])
    assert(catalanNumbers(5) == [1, 1, 2, 5, 14, 42])

test1()
