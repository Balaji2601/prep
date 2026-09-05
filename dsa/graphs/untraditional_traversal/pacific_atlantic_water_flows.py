# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# matrix

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific_visited = [[False]*n for _ in range(m)]
        atlantic_visited = [[False]*n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bound(i, j, visited, prev):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and heights[i][j] >= prev:
                return True
            return False

        def dfs(heights, i, j, visited):
            visited[i][j] = True

            for di, dj in directions:
                ni = i+di
                nj = j+dj
                # as prev is heights[i][j]
                if bound(ni, nj, visited, heights[i][j]):
                    dfs(heights, ni, nj, visited)
            
            
        for j in range(n):
            dfs(heights, 0, j, pacific_visited) # DFS from top row
            dfs(heights, m-1, j, atlantic_visited) # DFS from bottom row
        
        for i in range(m):
            dfs(heights, i, 0, pacific_visited) # DFS from left column
            dfs(heights, i, n-1, atlantic_visited) # DFS from right column
        
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    ans.append([i,j])

        return ans
