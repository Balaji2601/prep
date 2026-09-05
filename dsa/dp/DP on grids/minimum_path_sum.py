# https://leetcode.com/problems/minimum-path-sum/description

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        def solve(i,j):
            if i >= m or j >=n:
                return float("inf")
            if i == m-1 and j == n-1:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]

            right = grid[i][j] + solve(i,j+1)
            down = grid[i][j] + solve(i+1,j)
            
            dp[i][j] = min(right,down)
            return min(right,down)
        
        return solve(0,0)