# https://leetcode.com/problems/minimum-falling-path-sum/description/

from functools import cache
from typing import List

# recursion + memoization
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        directions = [(1,-1), (1,0), (1,1)]
        def bound(i,j):
            if 0<=i<n and 0<=j<n:
                return True
            return False

        @cache
        def solve(i,j):
            if i == n-1:
                return matrix[i][j]
            
            minVal = float("inf")
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                if bound(ni,nj):
                    minVal = min(matrix[i][j] + solve(ni,nj), minVal)
            
            return minVal

        ans = float("inf")
        for j in range(n):
            ans = min(ans,solve(0,j))
        return ans
    
# recursion + memoization with out cache
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        directions = [(1,-1), (1,0), (1,1)]
        def bound(i,j):
            if 0<=i<n and 0<=j<n:
                return True
            return False

        dp = [[None]*n for _ in range(n)]
        def solve(i,j):
            if i == n-1:
                return matrix[i][j]
            if dp[i][j] is not None:
                return dp[i][j]
            minVal = float("inf")
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                if bound(ni,nj):
                    minVal = min(matrix[i][j] + solve(ni,nj), minVal)
            dp[i][j] = minVal
            return dp[i][j]

        ans = float("inf")
        for j in range(n):
            ans = min(ans,solve(0,j))
        return ans

# bottom up
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        
        def bound(i,j):
            if 0<=i<m and 0<=j<n:
                return True
            return False

        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                    continue
                top_left = float("inf")
                up = float("inf")
                top_right = float("inf")
                if bound(i-1,j-1):
                    top_left =  dp[i-1][j-1]
                if bound(i-1,j):
                    up = dp[i-1][j]
                if bound(i-1,j+1):
                    top_right = dp[i-1][j+1]
                dp[i][j] = matrix[i][j] + min(top_left, up, top_right)
        
        return min(dp[n-1])