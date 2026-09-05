# https://leetcode.com/problems/combination-sum/description/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        def solve(i,target,temp,result):
            if target == 0:
                if temp not in result:
                    result.append(temp[:])
                return
            if i == n:
                return

            if candidates[i] <= target:
                temp.append(candidates[i])
                solve(i,target-candidates[i],temp,result)
                temp.pop()
            solve(i+1,target,temp,result)

        result = []
        temp = []
        solve(0,target,temp,result)
        return result
    

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        def solve(i,target,temp,result):
            if target == 0:
                result.append(temp[:])
                return
            if i == n:
                return
            
            if candidates[i] <= target:
                temp.append(candidates[i])
                solve(i,target-candidates[i],temp,result)
                temp.pop()
            solve(i+1,target,temp,result)

        result = []
        temp = []
        solve(0,target,temp,result)
        return result

# optimal 
# we do not need to sort
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def solve(i,target,temp,result):
            
            if target == 0:
                result.append(temp[:])
                return
            if i == n:
                return
            
            if candidates[i] <= target:
                temp.append(candidates[i])
                solve(i,target-candidates[i],temp,result)
                temp.pop()
            solve(i+1,target,temp,result)

        result = []
        temp = []
        solve(0,target,temp,result)
        return result