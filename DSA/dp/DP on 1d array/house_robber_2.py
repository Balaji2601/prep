# https://leetcode.com/problems/house-robber-ii/
# Intuition: Same approach as house robber 1 but with circular condition
# To solve the circular trick
# 1. We use the solve function first by stealing 1st house and skipping last house
# 2. We skip the first house and steal at the last
# And get maximum between the two approaches.
from typing import List


# recursion + memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums, i, n, dp):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]

            steal = nums[i] + solve(nums, i+2, n, dp)
            skip = solve(nums, i+1, n, dp)

            dp[i] = max(steal, skip)
            return dp[i]

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])
        
        dp1 = [-1]*(n+1)
        
        # steal_first ~ skip_last
        steal_first = solve(nums,0,n-1, dp1)

        # skip_first ~ steal_last
        dp2 = [-1]*(n+1)
        skip_first = solve(nums,1,n, dp2)
        

        return max(steal_first, skip_first)

# bottom up space: O(n)
class Solution2:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp1 = [0]*(n+1)

        dp1[1] = nums[0]

        for i in range(2, n):
            steal = nums[i-1] + dp1[i-2]
            skip = dp1[i-1]
            dp1[i] = max(steal, skip)
        
        dp2 = [0]*(n+1)
        dp2[2] = nums[1]

        for i in range(3, n+1):
            steal = nums[i-1] + dp2[i-2]
            skip = dp2[i-1]
            dp2[i] = max(steal, skip)
        
        return max(dp1[n-1], dp2[n])

# bottom up space: O(1)
class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[1], nums[0])
        
        a1 = nums[0]
        b1 = 0

        # skip last
        for i in range(2, n):
            steal = b1 + nums[i-1]
            skip = a1
            c1 = max(steal, skip)
            b1 = a1
            a1 = c1

        a2 = nums[1]
        b2 = 0
        # skip first
        for i in range(3, n+1):
            steal = b2 + nums[i-1]
            skip = a2
            c2 = max(steal, skip)
            b2 = a2
            a2 = c2

        return max(c1, c2)
