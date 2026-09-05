# https://leetcode.com/problems/triangle/description

from functools import cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def solve(i,j):
            if i == n:
                return 0

            return triangle[i][j] + min(solve(i+1,j), solve(i+1,j+1))
        
        return solve(0,0)