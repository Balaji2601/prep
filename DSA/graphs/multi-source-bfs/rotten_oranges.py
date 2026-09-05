# https://leetcode.com/problems/rotting-oranges/
# matrix

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def bound(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j] == 1 and not visited[i][j]:
                return True
            return False

        def bfs(rotten_oranges):
            q = deque()

            for i, j in rotten_oranges:
                visited[i][j] = True
                q.append((i,j))
            
            time = 0 
            while q:
                size = len(q)
                for _ in range(size):
                    i,j = q.popleft()
                    for di, dj in directions:
                        ni = i+di
                        nj = j+dj
                        if bound(ni, nj):
                            visited[ni][nj] = True
                            q.append((ni, nj))
                if q:
                    time += 1
            return time
        
        rotten_oranges = []
        fresh_oranges = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges.append((i,j))
                elif grid[i][j] == 2:
                    rotten_oranges.append((i,j))
        
        if len(fresh_oranges) == 0:
            return 0
        
        
        ans = bfs(rotten_oranges)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    return -1
        
        return ans