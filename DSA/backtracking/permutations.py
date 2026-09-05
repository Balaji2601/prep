# https://leetcode.com/problems/permutations/description/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = set()
        def solve(temp,result):
            if len(temp) == n:
                result.append(temp[:])
                return
            
            for i in range(n):
                if nums[i] not in s:
                    temp.append(nums[i])
                    s.add(nums[i])
                    solve(temp,result)
                    temp.pop()
                    s.remove(nums[i])
        
        result = []
        # We do not pass the idx because we loop i every idx ie [0,n-1]
        # using set helps the most
        solve([],result)
        return result