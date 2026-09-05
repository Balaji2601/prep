# https://leetcode.com/problems/fibonacci-number/description/

# brute force
# just recursion
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)

# recursion + memo
# passing dp array into solve function
class Solution2:
    def fib(self, n: int) -> int:

        def solve(n, dp):
            if n == 1:
                return 1
            if n == 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = solve(n-1, dp) + solve(n-2, dp)
            return dp[n]

        if n == 1:
            return 1
        if n == 0:
            return 0

        # took n+1 size
        # because if we want answer for n so we just return dp[n]
        # see below commented code
        dp = [-1]*(n+1)
        return solve(n, dp)

        # dp = [-1]*(n+1)
        # solve(n,dp)
        # return dp[n]

# recursion + memo 
# updating dp array globally
class Solution3:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def solve(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = solve(n-1) + solve(n-2)
            return dp[n]

        if n == 1:
            return 1
        if n == 0:
            return 0

        return solve(n)

# bottom up
# O(n) TC
# O(n) SC
class Solution4:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)

        # wkt, dp[i] = ith fibonocci number
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]

# bottom up with constant space
class Solution5:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1

        # for n = 2 we need to run this loop exactly once means 2-1 times
        # so for n we need to run this loop n-1 times ie from 1, n-1
        for _ in range(1, n):
            c = a+b
            a = b
            b = c

        return c