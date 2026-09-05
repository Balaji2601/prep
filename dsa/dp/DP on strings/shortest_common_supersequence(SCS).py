# https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1

# recursion
class Solution:
    def minSuperSeq(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        def solve(i,j):
            if i >= m:
                return n-j
            if j >= n:
                return m-i
            
            if s1[i] == s2[j]:
                return 1+solve(i+1,j+1)
            else:
                return 1+min(solve(i,j+1), solve(i+1,j))
                
        return solve(0,0)

# recursion+memoization
class Solution2:
    def minSuperSeq(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def solve(i,j):
            if i >= m:
                return n-j
            if j >= n:
                return m-i
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s2[j]:
                dp[i][j] = 1+solve(i+1,j+1)
                return 1+solve(i+1,j+1)
            else:
                dp[i][j] = 1+min(solve(i,j+1), solve(i+1,j))
                return 1+min(solve(i,j+1), solve(i+1,j))

        return solve(0,0)

# recursion + memoization with sending m,n reverse
class Solution3:
    def minSuperSeq(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def solve(m,n):
            if m == 0:
                return n
            if n == 0:
                return m
            if dp[m][n] != -1:
                return dp[m][n]
            
            if s1[m-1] == s2[n-1]:
                dp[m][n] = 1+solve(m-1,n-1)
                return 1+solve(m-1,n-1)
            else:
                dp[m][n] = 1+min(solve(m,n-1), solve(m-1,n))
                return 1+min(solve(m,n-1), solve(m-1,n))
                
        
        return solve(m,n)

# bottom up
class Solution4:
    def minSuperSeq(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(0,m+1):
            for j in range(0,n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

# using LCS
# A union B = A + B - (A intersection B)
class Solution5:
    def minSuperSeq(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        #LCS bottom up
        for i in range(0,m+1):
            for j in range(0,n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        LCS = dp[m][n]
        return m+n - LCS

