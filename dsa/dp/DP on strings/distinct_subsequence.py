# https://leetcode.com/problems/distinct-subsequences/description/

from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        
        @cache
        def solve(i,j):
            if j == n2:
                return 1
            
            if i == n1:
                return 0
            
            pick = 0
            if s[i] == t[j]:
                pick = solve(i+1,j+1)
            
            skip = solve(i+1,j)

            return pick + skip
        
        return solve(0,0)