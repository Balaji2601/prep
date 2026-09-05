# https://leetcode.com/problems/maximum-alternating-subsequence-sum/description/

from typing import List

# recursion + memo
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        # While every recursion call we have state changing
        # variables i, flag(True/False)
        # Flag is basically for when we take something from array
        # For the final answer we need to add something or subtract something
        # This flag variable will be helpful: 
        # 1. If flag == True: we add nums[i] to final answer meaning even
        # 2. flag == False: we subtract nums[i] from final answer meaning odd 
        # Consider flag as isEven boolean flag == 0 even, flag == 1 odd
        # If you see flag only changes while choosing something from the array, while skipping flag does not change.
        dp = [[-1]*2 for _ in range(n+1)]

        def solve(nums,i,flag):
            if i >= n:
                return 0
            if dp[i][flag] != -1:
                return dp[i][flag]
            
            if flag == 0: #even
                choose = solve(nums, i+1, 1) + nums[i] # change flag to 1
            else: #odd
                choose = solve(nums, i+1, 0) - nums[i] # change flag to 0

            skip = solve(nums, i+1, flag)

            dp[i][flag] = max(choose, skip)
            return dp[i][flag]

        return solve(nums,0,0) # flag is even for 0th index


#bottom up
class Solution2:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] represents maxAlternatingSum till ith index 
        # dp[i][0] meaning maxAlternatingSum till ith index if ai is added as even index into the 
        # subsequence we have earlier at dp[i-1][1] -> (i-1)th index at len(subsequence) odd.
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(1, n+1):
            # max(choose this ai, skip this ai)
            dp[i][0] = max(dp[i-1][1]-nums[i-1], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]+nums[i-1], dp[i-1][1])
        return max(dp[n][0], dp[n][1])