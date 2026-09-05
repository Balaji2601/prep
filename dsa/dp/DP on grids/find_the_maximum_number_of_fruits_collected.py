# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/

from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        m = len(fruits)
        n = len(fruits[0])
        dp = [[-1]*n for _ in range(m)]
        def bound(i,j):
            if 0<=i<m and 0<=j<n:
                return True
            return False

        # child 1 will collect only diagonal 
        # n-1 steps constraint
        def collectFruits1(fruits):
            ans = 0
            for i in range(n):
                ans += fruits[i][i]
            return ans

        d2 = [(1,-1),(1,0),(1,1)]
        d3 = [(-1,1),(0,1),(1,1)]

        # we donot need step count because child 2 moves 1 unique extra row 
        # after every step he makes and will eventually makes n-1 steps at last row
        # and last row element accessable for child 2 is the destination cell
        def collectFruits2(i,j,fruits):
            # this cell fruit is already collected by child 1
            if i == m-1 and j == n-1:
                return 0
            # child 2 cannot enter into i > j case 
            # because if got into bottom left area(below diagonal)
            # child cannot reach destination in n-1 steps
            if i == j or i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            val = -float("inf")
            for di,dj in d2:
                ni = i+di
                nj = j+dj
                if bound(ni,nj):
                    val = max(val, fruits[i][j]+collectFruits2(ni,nj,fruits))
            
            dp[i][j] = val
            return dp[i][j]
        
        # we donot need step count because child 3 moves 1 unique extra column 
        # after every step he makes and will eventually makes n-1 steps at last column
        # and last column element accessable for child 3 is the destination cell
        def collectFruits3(i,j,fruits):
            if i == m-1 and j == n-1:
                return 0
            # child 3 cannot enter into i < j case 
            # because if got into top right area(above diagonal)
            # child cannot reach destination in n-1 steps
            if i == j or i < j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            val = -float("inf")
            for di,dj in d3:
                ni = i+di
                nj = j+dj
                if bound(ni,nj):
                    val = max(val, fruits[i][j]+collectFruits3(ni,nj,fruits))
            dp[i][j] = val
            return dp[i][j]

        c1 = collectFruits1(fruits)
        c2 = collectFruits2(0,n-1,fruits)
        c3 = collectFruits3(n-1,0,fruits)
        return c1+c2+c3