# https://leetcode.com/problems/house-robber/description/

# Intution: You have two choices to choose at ith house
# 1. Steal the current house
# 2. Skip the current house
# If you choose 1: You must have to skip the i+1th house and go to i+2th house
# If you choose 2: As you skipped the current house you are allowed to go i+1th house 
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(nums, i):
            if i >= n:
                return 0

            # Option1: Steal this ith house get nums[i] and go to i+2 house
            steal = nums[i] + solve(nums, i+2)

            # Option2: Skip this ith house get 0 and go to i+1 house
            skip = 0 + solve(nums, i+1)

            return max(steal, skip)

        return solve(nums, 0) # start at 0th index


# recursion + memo
class Solution2:
    def rob(self, nums: List[int]) -> int:
        # See the constraints n will be max 100
        dp = [-1]*(101) # memoize
        n = len(nums)
        def solve(nums, i):
            if i >= n:
                return 0
            # if i is visited earlier
            if dp[i] != -1:
                return dp[i]
            # on ith index we have to chances either we have to steal this house or skip this, 
            # so if steal we get the money from ith house and we cannot go to next house, so we go to i+2th house
            steal = nums[i] + solve(nums, i+2)
            # else skip the ith house move to i+1 house, skipping this ith house gives 0 in return
            skip = 0 + solve(nums, i+1)
            
            dp[i] = max(steal, skip)
            return dp[i]

        return solve(nums, 0) # nums, which index we are starting


# bottom up with dp initialization [-1]*(n+1)
class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[-1]
        
        if n == 2:
            return max(nums[-1], nums[-2])
        
        dp = [-1]*(n+1)

        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, n+1):
            steal = nums[i-1]+dp[i-2]
            skip = dp[i-1]
            dp[i] = max(steal, skip)
        
        return dp[n]

# bottom up with dp initialization [0]*(n+1)
class Solution4:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Max stolen money till i = 1 house is nums[i - 1] ie 0
        if n == 1:
            return nums[0]
        
        dp = [0]*(n+1)

        dp[1] = nums[0]

        for i in range(2,n+1):
            # ith house in dp is i-1 index in nums
            steal = nums[i-1] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(steal, skip)
        
        return dp[n]

        
class Solution5:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        a = nums[0]
        b = 0

        for i in range(2, n+1):
            steal = b + nums[i-1]
            skip = a
            c = max(steal, skip)
            b = a
            a = c

        return c