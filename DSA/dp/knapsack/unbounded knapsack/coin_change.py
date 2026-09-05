# https://leetcode.com/problems/coin-change/description/

from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def solve(i, amount):
            if amount == 0:
                return 0

            if i >= n:
                return float("inf")

            take = float("inf")
            if coins[i] <= amount:
                take = 1 + solve(i, amount - coins[i])
            skip = solve(i + 1, amount)

            return min(take, skip)

        ans = solve(0, amount)

        return -1 if ans == float("inf") else ans


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def solve(n, amount):
            if n == 0:
                return float("inf")
            if amount == 0:
                return 0
            
            pick = float("inf")
            if coins[n-1] <= amount:
                pick = 1+solve(n, amount-coins[n-1])
            skip = solve(n-1,amount)
            return min(pick, skip)
        
        ans = solve(n,amount)
        if ans == float("inf"):
            return -1
        return ans

# recursion + memo
# starting with length n-1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[None]*(amount+1) for _ in range(n+1)]

        def solve(n, amount):
            if n == 0:
                return float("inf")
            if amount == 0:
                return 0
            
            if dp[n][amount] is not None:
                return dp[n][amount]
            
            pick = float("inf")
            if coins[n-1] <= amount:
                pick = 1+solve(n, amount-coins[n-1])
            skip = solve(n-1,amount)
            dp[n][amount] = min(pick, skip)
            return dp[n][amount]
        
        ans = solve(n,amount)
        if ans == float("inf"):
            return -1
        return ans
    
# bottom up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]

        for j in range(0,amount+1):
            dp[0][j] = float("inf")
        

        for i in range(1,n+1):
            for j in range(1, amount+1):
                pick = float("inf")
                if coins[i-1] <= j:
                    pick = 1+dp[i][j-coins[i-1]]
                skip = dp[i-1][j]

                dp[i][j] = min(pick,skip)
        
        if dp[n][amount] == float("inf"):
            return -1
        return dp[n][amount] 