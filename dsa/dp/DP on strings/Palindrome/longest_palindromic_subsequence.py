# https://leetcode.com/problems/longest-palindromic-subsequence/

# intuition: LCS between s and s[::-1] gives longest palidromic subsequence
# recursion + memoization
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s1 = s
        s2 = s[::-1]
        dp = [[-1]*n for _ in range(n)]
        
        def solve(i,j):
            if i == n or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s2[j]:
                dp[i][j] = 1+solve(i+1,j+1)
                return dp[i][j]
            else:
                dp[i][j] = max(solve(i+1,j), solve(i,j+1))
                return dp[i][j]
        
        return solve(0,0)

# using LCS approach but starting at s i = 0 to j = n-1 and 
# if s[i] == s[j] we are adding 2 
# because we include both in the palindromic seq
# and if i == j we return 1 
# as s = "a" has one longestPalindromeSubseq
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        def solve(i,j):
            if i > j:
                return 0
            if i == j:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                dp[i][j] = 2+solve(i+1, j-1)
                return 2+solve(i+1, j-1)
            else:
                dp[i][j] = max(solve(i+1,j), solve(i,j-1))
                return max(solve(i+1,j), solve(i,j-1))
            
        return solve(0,n-1)

# using blue print method
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # state defination: dp[i][j] means s[i:j+1] LPS(longestPalindromeSubseq) for s[i:j+1]
        dp = [[0]*(n) for _ in range(n)]

        for L in range(1,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1] # meaning in s[0:n] the LPS for s[0:n]