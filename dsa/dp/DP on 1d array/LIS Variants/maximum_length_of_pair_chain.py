# https://leetcode.com/problems/maximum-length-of-pair-chain/description/

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        # sort by 1st value of each pair
        pairs.sort()
        dp = [[-1]*(n+1) for _ in range(n+1)]
        def solve(i, prev):
            if i >= n:
                return 0
            if prev != -1 and dp[i][prev] != -1:
                return dp[i][prev]

            choose = 0
            if prev == -1 or pairs[prev][1] < pairs[i][0]:
                choose = 1+solve(i+1,i)
            skip = solve(i+1,prev)
            
            if prev != -1:
                dp[i][prev] = max(skip, choose)

            return max(skip, choose)
            

        return solve(0,-1) # curr, prev


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        # sort by 1st value of each pair
        pairs.sort()
        dp = [1]*n

        longestChain = 1
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], 1+dp[j])
                    longestChain = max(longestChain, dp[i])
        
        return longestChain