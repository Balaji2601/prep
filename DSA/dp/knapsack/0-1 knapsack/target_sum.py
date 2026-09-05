# https://leetcode.com/problems/target-sum/description

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        dp = {}
        def solve(i, curr_val):
            if i == n:
                if target == curr_val:
                    return 1
                return 0
            if (i,curr_val) in dp:
                return dp[(i,curr_val)]
            add = solve(i+1, curr_val+nums[i])
            sub = solve(i+1, curr_val-nums[i])

            dp[(i,curr_val)] = add+sub
            return dp[(i,curr_val)]
        
        return solve(0,0)