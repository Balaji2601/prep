# https://leetcode.com/problems/number-of-islands/
# matrix

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bound(i,j, grid, visited):
            if (0 <= i < m) and (0 <= j < n) and (grid[i][j] == "1") and not visited[i][j]:
                return True
            return False

        def DFS(grid, i, j, visited):
            visited[i][j] = True

            # up (i-1, j)
            if bound(i-1, j, grid, visited):
                DFS(grid, i-1, j, visited)

            # down (i+1, j)
            if bound(i+1, j, grid, visited):
                DFS(grid, i+1, j, visited)

            # right (i, j+1)
            if bound(i, j+1, grid, visited):
                DFS(grid, i, j+1, visited)

            # left (i, j-1)
            if bound(i, j-1, grid, visited):
                DFS(grid, i, j-1, visited)

        
        
        visited = [[False] * n for _ in range(m)]
        
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    DFS(grid, i, j, visited)
                    count += 1
        
        return count
