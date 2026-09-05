# https://leetcode.com/problems/palindromic-substrings/

# brute_force
# O(n**3)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1
        
        return count


# O(n**2)
# recursion + memoization in the check_palindrome function for s
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*(n) for _ in range(n)]

        def check_palindrome_without_memo(i,j,s):
            if i > j:
                return True

            if s[i] == s[j]:
                return check_palindrome_without_memo(i+1, j-1, s)
            
            return False

        def check_palindrome_without_recursion(i,j,s):
            while i <= j:
                if s[i] == s[j]:
                    i -= 1
                    j -= 1
                else:
                    return False
            return True


        def check_palindrome(i,j,s):
            if i > j:
                return True
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = check_palindrome(i+1, j-1, s)
                return check_palindrome(i+1, j-1, s)
            
            dp[i][j] = False
            return False

        count = 0
        for i in range(n):
            for j in range(i,n):
                if check_palindrome(i,j,s):
                    count += 1
        
        return count


# blue print
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # state defination: if dp[i][j] == True means s[i:j+1] is a palindrome
        dp = [[False]*(n) for _ in range(n)]

        count = 0
        for L in range(1,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    dp[i][j] = (s[i] == s[j]) and (dp[i+1][j-1])

                if dp[i][j]:
                    count += 1
        
        return count
    
# blue print(another way)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # state defination: if dp[i][j] == True means s[i:j+1] is a palindrome
        dp = [[False]*(n) for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        count = 0
        for L in range(2,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    dp[i][j] = (s[i] == s[j]) and (dp[i+1][j-1])

                if dp[i][j]:
                    count += 1
        
        return count


# O(n**2)
# Smart approach with even, odd 
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def check(i,j):
            ans = 0
            while i >= 0 and j < n and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
            
            return ans

        count = 0
        for i in range(n):
            count += check(i,i)+check(i,i+1) # even + odd
        
        return count