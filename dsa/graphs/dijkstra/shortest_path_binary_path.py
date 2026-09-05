# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# matrix

import heapq
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = [[float("inf")]*n for _ in range(n)]
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

        def bound(i, j):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                return True
            return False

        if grid[0][0] == 1:
            return -1
        pq = [(0, 0, 0)] # dist, x, y
        result[0][0] = 0

        while pq:
            dist, i, j = heapq.heappop(pq)

            if dist > result[i][j]:
                continue
            for di, dj in directions:
                ni = i+di
                nj = j+dj
                if bound(ni, nj) and dist+1 < result[ni][nj]:
                    result[ni][nj] = dist+1
                    heapq.heappush(pq, (dist+1, ni, nj))
        
        if result[n-1][n-1] == float("inf"):
            return -1

        return result[n-1][n-1] + 1



