# https://leetcode.com/problems/climbing-stairs/
# Intution1: You have two choices at ith stair
# 1. You can go i+1th stair
# 2. You can go i+2th stair
# Intution2: Reverse thinking
# You are at ith stair
# 1. You came here from i-1th stair
# 2. You came here from i-2th stair

# brute force
class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n):
            if n == -1:
                return 0
            if n == 0:
                return 1
            
            one_step = solve(n-1)
            two_step = solve(n-2)
            
            return one_step + two_step
        
        return solve(n)

# recursion + memo
class Solution2:
    def climbStairs(self, n: int) -> int:
        # At each step we have two possibilites either we can climb 
        # one step or two steps

        # solving this qn from n not from 0

        # take a dp array of size n+1
        dp = [-1]*(n+1)
        
        def solve(n):
            if n == -1:
                return 0
            if n == 0:
                return 1
            if dp[n] != -1:
                return dp[n]
            
            # one_step down ---> no of ways
            one_step = solve(n-1)
            # two_step down ---> no of ways
            two_step = solve(n-2)
            
            dp[n] = one_step + two_step

            return dp[n]

        return solve(n)

# bottom up
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [-1]*(n+1)
        dp[1] = 1 # no of ways to climb 1st stair
        dp[2] = 2 # no of ways to climb 2nd stair

        # dp[i] meaning no of ways to climb ith stair
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]

# bottom up with constant space
class Solution4:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a = 1
        b = 2
        for i in range(3,n+1):
            c = a+b
            a = b
            b = c
        
        return c