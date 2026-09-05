from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def solve(i,amount):
            if amount == 0:
                return 1
            
            if i >= n:
                return 0
            
            take = 0
            if coins[i] <= amount:
                take = solve(i,amount-coins[i])
            skip = solve(i+1,amount)

            return take + skip
        
        return solve(0,amount)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        @cache
        def solve(n, amount):
            if amount == 0:
                return 1
            
            if n == 0:
                return 0
            
            pick = 0
            if coins[n-1] <= amount:
                pick = solve(n, amount-coins[n-1])
                
            skip = solve(n-1,amount)

            return pick+skip
        
        return solve(n, amount)

