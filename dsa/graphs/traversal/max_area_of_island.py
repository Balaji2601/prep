# https://leetcode.com/problems/max-area-of-island/
# matrix

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        

        def bound(grid, i, j, visited):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1 and not visited[i][j]:
                return True
            return False

        def DFS(grid, i, j, visited, count):
            visited[i][j] = True
            count[0] += 1

            #up (i-1,j)
            if bound(grid, i-1, j, visited):
                DFS(grid, i-1, j, visited,count)
            
            #down (i+1,j)
            if bound(grid, i+1,j, visited):
                DFS(grid, i+1,j, visited,count)

            #left (i,j-1)
            if bound(grid, i,j-1, visited):
                DFS(grid, i,j-1, visited,count)
            #right (i,j+1)
            if bound(grid, i,j+1, visited):
                DFS(grid, i,j+1, visited,count)

        visited = [[False]*cols for _ in range(rows)]
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    count = [0]
                    DFS(grid, i, j, visited, count)
                    ans = max(ans, count[0])
        
        return ans


