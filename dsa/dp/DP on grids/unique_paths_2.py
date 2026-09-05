# https://leetcode.com/problems/unique-paths-ii/description/

from typing import List

# if there is a obstacle when we check bound introduced 
# obstacleGrid[i][j] == 1 means if there is a obstacle 
# we return 0 means this path going from (0,0) to (m-1,n-1)
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n for _ in range(m)]

        def solve(i,j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            right = solve(i,j+1)
            down = solve(i+1,j)
            
            dp[i][j] = right+down
            return right+down
        
        return solve(0,0)


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]

        # corner case
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp[0][0] = 1
        def bound(i,j):
            if 0<=i<m and 0<=j<n and obstacleGrid[i][j] == 0:
                return True
            return False

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    if bound(i-1,j):
                        dp[i][j] += dp[i-1][j]
                    if bound(i,j-1):
                        dp[i][j] += dp[i][j-1]
        
        return dp[m-1][n-1]


class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        
        # corner case
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp[0][0] = 1

        for j in range(1,n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        for i in range(1,m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]