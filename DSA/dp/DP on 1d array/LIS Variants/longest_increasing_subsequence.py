# https://leetcode.com/problems/longest-increasing-subsequence/description/

from typing import List

# recursion + memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*n+1 for _ in range(n+1)] # curr, prev indices

        def solve(i, prev):
            if i >= n:
                return 0
            # prev!=-1 : because dp[i][-1] is wrong 
            if prev != -1 and dp[i][prev] != -1:
                return dp[i][prev]

            choose = 0 # if the below condition doesnot meet then choose will be not initialized,
            # so by initializing choose to 0 will not cause an error
            if prev == -1 or nums[prev] < nums[i]:
                choose = 1+solve(i+1, i)

            skip = solve(i+1, prev)

            if prev != -1:
                dp[i][prev] = max(choose, skip)

            return max(choose, skip)

        return solve(0,-1)

# bottom up
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n

        maxLIS = 1
        # for every nums[i] check if nums[j] < nums[i]
        # if the condition is satisfied we need to update the dp[i] as max(1+dp[j], dp[i])
        for i in range(0, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(1+dp[j], dp[i])
                    maxLIS = max(maxLIS, dp[i])

        return maxLIS