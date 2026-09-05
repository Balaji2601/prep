# https://leetcode.com/problems/path-with-minimum-effort/description/

import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bound(i, j):
            if 0 <= i < rows and 0 <= j < cols:
                return True
            return False
        result = [[float("inf")]*cols for _ in range(rows)]

        result[0][0] = 0
        pq = [(0,0,0)] # min_dist, x, y

        while pq:
            # dist is effort: to come to this i,j taken effort
            dist, i, j = heapq.heappop(pq)

            if dist > result[i][j]:
                continue
            val = heights[i][j]
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if bound(ni, nj):
                     # the effort taken to get here from i,j to ni, nj 
                     # is abs(val---->heights[i][j]-heights[ni][nj]) 
                    curr_effort = abs(val - heights[ni][nj])
                    # calcuate which is more curr_effort or dist(parent_node_effort)
                    curr_result = max(dist, curr_effort)
                    if curr_result < result[ni][nj]:
                        result[ni][nj] = curr_result
                        heapq.heappush(pq,(curr_result, ni, nj))
            
        return result[rows-1][cols-1]




