# https://leetcode.com/problems/longest-palindromic-substring/description/

# print longest palindromic substring

# brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        ans = ""
        max_length = -float("inf")
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        ans = s[i:j+1]
        
        return ans


# with check_palindrome recursion + memoization
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]

        def check(i,j):
            if i > j:
                return True
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = check(i+1, j-1)
                return check(i+1, j-1)
            dp[i][j] = False
            return False

        ans = ""
        max_length = -float("inf")
        for i in range(n):
            for j in range(i,n):
                if check(i,j):
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        ans = s[i:j+1]
        
        return ans

# with blueprint
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]

        max_length = -float("inf")
        for L in range(1, n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp[i][j] = True
                elif i+1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                
                if dp[i][j]:
                    if max_length < j-i+1:
                        max_length = j-i+1
                        start_idx = i
                        end_idx = j
        
        return s[start_idx:end_idx+1]