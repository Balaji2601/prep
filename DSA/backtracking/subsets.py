# https://leetcode.com/problems/subsets/description/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def solve(i,temp,result):
            if i == n:
                result.append(temp[:])
                return
            
            temp.append(nums[i])
            solve(i+1, temp, result)
            temp.pop()
            solve(i+1, temp, result)
        
        result = []
        solve(0,[], result)
        return result