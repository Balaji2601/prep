# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
# https://www.youtube.com/watch?v=ZIFAFLARoLs
# matrix

from collections import deque
from typing import List

# As going to a cell it only costs either 0/1 right? so it is 0-1 BFS
# This problem is about going from src to dst and SSSP(single source shortest path)
# Not as 01 matrix
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        result = [[float("inf")]*n for _ in range(m)]
        if grid[0][0] == 1:
            result[0][0] = 1
            q = deque([(1,0,0)])
        else:
            result[0][0] = 0
            q = deque([(0,0,0)])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            cost, i, j = q.popleft()
            for di, dj in directions:
                ni = i+di
                nj = j+dj
                if 0 <= ni < m and 0 <= nj < n:
                    curr_node_cost = cost+grid[ni][nj]
                    if curr_node_cost < result[ni][nj]:
                        result[ni][nj] = curr_node_cost
                        if grid[ni][nj]:
                            # the cost took to get to this node is 1 from (i,j) to (ni,nj)
                            q.append((curr_node_cost, ni, nj))
                        else:
                            # the cost took to get to this node is 0 from (i,j) to (ni,nj)
                            # important why appending at the left of queue
                            # for reference see this video
                            # https://www.youtube.com/watch?v=U83oTSsjNqY
                            q.appendleft((curr_node_cost, ni, nj)) 
        
        return result[m-1][n-1] < health