# https://leetcode.com/problems/maximum-number-of-points-with-cost/description/

from typing import List

# brute force
# O(m*n*n)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [[0]*n for _ in range(m)]

        for j in range(n):
            dp[0][j] = points[0][j]
        
        for i in range(1,m):
            for j in range(n):
                val = -float("inf")
                for k in range(n):
                    val = max(points[i][j]+dp[i-1][k]-abs(j-k),val)
                dp[i][j] = val
        return max(dp[m-1])


# optimal solution
# O(m*n)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        prev = [0]*n
        for j in range(n):
            prev[j] = points[0][j]
        
        
        for i in range(1,m):
            left = [0]*n
            right = [0]*n
            
            left[0] = prev[0]
            for k in range(1,n):
                left[k] = max(prev[k], left[k-1]-1)
            
            right[n-1] = prev[n-1]
            for k in range(n-2,-1,-1):
                right[k] = max(prev[k], right[k+1]-1)
            
            curr = [0]*n
            for k in range(n):
                curr[k] = points[i][k] + max(left[k], right[k])
            
            prev = curr
        
        return max(prev)
