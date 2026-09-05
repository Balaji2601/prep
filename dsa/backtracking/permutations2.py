# https://leetcode.com/problems/permutations-ii/description/

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = set()
        result_set = set()
        def solve(temp,result):
            if len(temp) == n:
                temp_tuple = tuple(temp)
                if temp_tuple not in result_set:
                    result.append(temp[:])
                    result_set.add(temp_tuple)
                return 
            
            for i,val in enumerate(nums):
                if i not in s:
                    temp.append(val)
                    s.add(i)
                    solve(temp,result)
                    temp.pop()
                    s.remove(i)
        
        result = []
        solve([],result)
        return result