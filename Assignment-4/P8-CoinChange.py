"""
Question 8: CoinChange
Given a list of coin denominations and a target sum, return the number of possible ways to make 
change for that sum.


Tests used from https://leetcode.com/problems/coin-change-ii/
"""

# Strategy: 2-dim DP memoization + recursion 
# idea: can choose to use first coin or not. Then there are (coinChange(use first) + coinChange(don't use first)) ways
# recursion will stop when sum <= 0

# Time taken: 10 minutes

def change(amount: int, coins: list[int]) -> int:
    memo = {}# maps (amount,len(coins)) to number of ways 
    
    def recHelper(amount:int, coins:list[int]) -> int:
        # memo and base cases
        if (amount, len(coins)) in memo:
            return memo[(amount, len(coins))]
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        
        # recursive case, can either use first coin or not
        useFirst = recHelper(amount-coins[0], coins)
        loseFirst = recHelper(amount, coins[1:])

        memo[(amount, len(coins))] = useFirst+loseFirst
        return useFirst+loseFirst
    return recHelper(amount,coins)


"""
------------------------------
            TESTS
------------------------------
"""

# NOTE: this solution passes al tests on https://leetcode.com/problems/coin-change-ii/

def tests():
    assert(change(5,[1,2,5]) == 4)

    assert(change(3,[2]) == 0)

    assert(change(10,[10]) == 1)

tests()