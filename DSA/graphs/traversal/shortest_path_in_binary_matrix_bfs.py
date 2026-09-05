# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# matrix

from typing import List


from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        n = len(grid)
        visited = [[False]*n for _ in range(n)]

        def bound(i, j):
            if 0 <= i < n and 0 <= j < n and not visited[i][j] and grid[i][j] == 0:
                return True
            return False
        

        if grid[0][0] != 0:
            return -1

        q = deque([(0,0,1)])
        visited[0][0] = True

        while q:
            i, j, dist = q.popleft()
            if (i,j) == (n-1, n-1):
                return dist
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if bound(ni, nj):
                    visited[ni][nj] = True
                    q.append((ni, nj, dist+1))
        return -1