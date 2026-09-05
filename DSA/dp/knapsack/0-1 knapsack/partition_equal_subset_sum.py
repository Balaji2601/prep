# https://leetcode.com/problems/partition-equal-subset-sum/description/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}
        def solve(i, curr_sum, rem_sum):
            if curr_sum == rem_sum:
                return True
            
            if i >= n or curr_sum > rem_sum:
                return False

            if (i,curr_sum, rem_sum) in dp:
                return dp[(i,curr_sum, rem_sum)]

            if solve(i+1, curr_sum+nums[i], rem_sum-nums[i]):
                dp[(i,curr_sum, rem_sum)] = True
                return dp[(i,curr_sum, rem_sum)]
            
            if solve(i+1, curr_sum, rem_sum):
                dp[(i,curr_sum, rem_sum)] = True
                return dp[(i,curr_sum, rem_sum)]
            
            dp[(i,curr_sum, rem_sum)] = False
            return dp[(i,curr_sum, rem_sum)] 
        
        # we cannot partition the given nums into two if the sum of nums is odd
        # we can only partition if it is even
        s = sum(nums)
        if s % 2 == 1:
            return False
        return solve(0, 0, s)