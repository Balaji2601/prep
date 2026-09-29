# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/description

from functools import cache

# Revise
# Validate parenthesis using OpenCount
# m+n-1 length approach is important
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1), (1,0)]
        if (m + n - 1) % 2 == 1 or grid[0][0] == ")" or grid[m-1][n-1] == "(":
            return False

        def bound(i,j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False
        
        @cache
        def solve(i,j,OpenCount):
            OpenCount += 1 if grid[i][j] == "(" else -1
            if OpenCount < 0:
                return False

            if i == m-1 and j == n-1:
                return OpenCount == 0
            
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                if bound(ni,nj):
                    if solve(ni,nj, OpenCount):
                        return True
            
            return False
        
        return solve(0,0,0)