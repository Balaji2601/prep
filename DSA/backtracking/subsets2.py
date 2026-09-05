# https://leetcode.com/problems/subsets-ii/description/

from typing import List

# brute force
# checking temp in result is not optimal
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        def solve(i,temp,result):
            if i == n:
                if temp not in result:
                    result.append(temp[:])
                return
            
            temp.append(nums[i])
            solve(i+1,temp,result)
            temp.pop()
            solve(i+1,temp,result)
        
        result = []
        solve(0,[], result)
        return result

# skip the same elements
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        def solve(i,temp,result):
            if i == n:
                if temp not in result:
                    result.append(temp[:])
                return
            
            temp.append(nums[i])
            solve(i+1,temp,result)
            temp.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            solve(i+1,temp,result)
        
        result = []
        solve(0,[], result)
        return result