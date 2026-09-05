# https://leetcode.com/problems/01-matrix/description/
# matrix

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[-1]*n for _ in range(m)]
        q = deque([])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    q.append((i,j))

        def bound(i,j):
            if 0<=i<m and 0<=j<n and result[i][j] == -1:
                return True
            return False
        
        while q:
            i,j = q.popleft()
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                if bound(ni, nj):
                    result[ni][nj] = result[i][j] + 1
                    q.append((ni, nj))
        
        return result

