# https://leetcode.com/problems/palindrome-partitioning-ii/description/


# solve(i,j) -> gives output min no of cuts required to make a string s[i:j] j inclusive 
# to make each substring a palindrome.
# recursion
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:
            return 0

        def solve(i,j):
            if i >= j:
                return 0
            if s[i:j+1] == s[i:j+1][::-1]: # check palindrome s[i,j] if true we dont require any cuts
                return 0
            
            ans = float("inf")

            for k in range(i, j):
                ans = min(1+solve(i,k)+solve(k+1,j),ans)
            
            return ans
        
        return solve(0,n-1)


# recursion + memoization
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:
            return 0

        dp = [[-1]*(n+1) for _ in range(n+1)]
        # solve(i,j) -> gives output min no of cuts required to make a string s[i:j] j inclusive
        def solve(i,j):
            if i >= j:
                return 0
            if s[i:j+1] == s[i:j+1][::-1]: # check palindrome s[i,j] if true we dont require any cuts
                dp[i][j] = 0
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = float("inf")

            for k in range(i, j):
                ans = min(1+solve(i,k)+solve(k+1,j),ans)
            
            dp[i][j] = ans
            return ans
        
        return solve(0,n-1)

# recursion + memoization with palidrome check with bottom up(blue print)
# TLE in leetcode
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:
            return 0
        
        dp1 = [[False]*(n+1) for _ in range(n+1)]

        for L in range(1,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp1[i][j] = True
                elif i+1 == j:
                    dp1[i][j] = s[i] == s[j]
                else:
                    dp1[i][j] = s[i] == s[j] and dp1[i+1][j-1]
        

        dp = [[-1]*(n+1) for _ in range(n+1)]
        # solve(i,j) -> gives output min no of cuts required to make a string s[i:j] j inclusive
        def solve(i,j):
            if i >= j:
                return 0
            if dp1[i][j]:
                dp[i][j] = 0
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = float("inf")

            for k in range(i, j):
                ans = min(1+solve(i,k)+solve(k+1,j),ans)
            
            dp[i][j] = ans
            return ans
        
        return solve(0,n-1)


# optimal solution O(n^2)
# using blue print for checking the palindrome
# looping on every letter index i 
# if the blue print array dp[0][i] -> true meaning s[0:i] including letter at index i a palindrome 
# then we do not need to cut s[0:i]
# else s[0:i] is not a palindrome then we cut from k = 0 to i
# we maintain dp2 of length n and state defination of dp[i] is minimum no of cuts required to palindromic partition 
# for s[0:i] so we return dp[n-1] which gives minimun no of cuts to make s a palindromic partition.
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp1 = [[False]*n for _ in range(n)]

        for L in range(1,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp1[i][j] = True
                elif i + 1 == j:
                    dp1[i][j] = (s[i] == s[j])
                else:
                    dp1[i][j] = (s[i] == s[j] and dp1[i+1][j-1])
        
        # state defination: dp2[i] stores minimum no of cuts required to make a string s[0:i] i inclusive a palindrome
        # initially we dont know how many cuts required so we make to float("inf") if something comes up into dp2 will be
        # lesser than float("inf") right.
        dp2 = [float("inf")]*n
        
        for i in range(n):
            if dp1[0][i] == True:
                dp2[i] = 0
            else:
                for k in range(0,i):
                    if (dp1[k+1][i] == True) and (dp2[k]+1 < dp2[i]):
                        dp2[i] = 1+dp2[k]
        
        return dp2[n-1]
