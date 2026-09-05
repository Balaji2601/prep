# https://leetcode.com/problems/map-of-highest-peak/description/
# matrix

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        q = deque()
        heights = [[-1]*n for _ in range(m)]
        directions = [(1,0), (0,-1), (-1,0), (0,1)]
        visited = [[False]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    heights[i][j] = 0
                    visited[i][j] = True
        
        def bound(i,j):
            if 0<=i<m and 0<=j<n and not visited[i][j] and isWater[i][j] == 0:
                return True
            return False

        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                heights[i][j] = level

                for di, dj in directions:
                    ni = i+di
                    nj = j+dj

                    if bound(ni, nj):
                        q.append((ni, nj))
                        visited[ni][nj] = True

            if q:
                level += 1
        
        return heights

# We can solve this question like below as well because we are not returning the level and we do not require 
# level because storing them in result will help us. So for result (ni,nj) we can get the result from (i,j)
# understand that multi-source bfs is appending multiple sources before while loop not about the levels
# We store levels when qn demands(like for rotten oranges) or 
# when finding the diameter of a graph see folder(diameter-of-a-graph) in this repo.
# So if the popped element already stores what qn demands then levels are not needed.
# Below approach is same as 01_matrix.py in this folder.
class Solution2:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        q = deque()
        heights = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    heights[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bound(i,j):
            # heights[i][j] == -1 meaning unvisited thing and it is land obviusly
            # as we populated heights[i][j] with 0 when isWater[i][j]
            if 0<=i<m and 0<=j<n and heights[i][j] == -1:
                return True
            return False

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if bound(ni, nj):
                    heights[ni][nj] = heights[i][j] + 1
                    q.append((ni, nj))

        return heights