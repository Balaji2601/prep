# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/

from typing import List

# brute force 
# backtracking
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        result = []
        def solve(i,j,temp):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if i == m-1 and j == n-1:
                temp.append(grid[i][j])
                result.append(temp[:])
                temp.pop()
                return
            
            temp.append(grid[i][j])
            right = solve(i,j+1, temp)
            down = solve(i+1,j, temp)
            temp.pop()
        
        solve(0,0,[])
        ans = -float("inf")
        for arr in result:
            val = 1
            for ele in arr:
                val *= ele
            ans = max(val, ans)

        return ans % MOD if ans >= 0 else -1


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        dp = [[(-float("inf"),float("inf"))]*n for _ in range(m)]
        def bound(i,j):
            if 0<=i<m and 0<=j<n:
                return True
            return False

        def solve(i,j):
            if i == m-1 and j == n-1:
                return (grid[i][j], grid[i][j])

            if dp[i][j] != (-float("inf"),float("inf")):
                return dp[i][j]

            maxVal = -float("inf")
            minVal = float("inf")

            # right
            ni = i
            nj = j+1

            if bound(ni,nj):
                rightMax, rightMin = solve(ni,nj)
                maxVal = max(maxVal, grid[i][j]*rightMax, grid[i][j]*rightMin)
                minVal = min(minVal, grid[i][j]*rightMax, grid[i][j]*rightMin)

            # down
            ni = i+1
            nj = j
            if bound(ni,nj):
                downMax, downMin = solve(ni,nj)
                maxVal = max(maxVal, grid[i][j]*downMax, grid[i][j]*downMin)
                minVal = min(minVal, grid[i][j]*downMax, grid[i][j]*downMin)
            dp[i][j] = (maxVal, minVal)
            return (maxVal, minVal)
        
        return solve(0,0)[0] % MOD if solve(0,0)[0] >= 0 else -1