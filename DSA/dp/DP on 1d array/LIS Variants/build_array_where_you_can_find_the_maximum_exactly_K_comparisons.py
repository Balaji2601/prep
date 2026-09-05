# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[[-1]*101 for _ in range(51)] for _ in range(51)]
        def solve(idx, searchCost, maxSoFar):
            if idx == n:
                if searchCost == k:
                    return 1
                return 0
            
            if dp[idx][searchCost][maxSoFar] != -1:
                return dp[idx][searchCost][maxSoFar]

            result = 0
            for i in range(1,m+1):
                if i > maxSoFar:
                    result = (result+solve(idx+1,searchCost+1,i))%MOD
                else:
                    result = (result+solve(idx+1,searchCost,maxSoFar))%MOD
            
            dp[idx][searchCost][maxSoFar] = result%MOD
            
            return result%MOD
        
        return solve(0,0,0)