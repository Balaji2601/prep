# https://leetcode.com/problems/combinations/description/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]

        def solve(i,temp,result,k):
            if len(temp) == k:
                result.append(temp[:])
                return
            if i == n:
                return

            temp.append(nums[i])
            solve(i+1,temp,result,k)
            temp.pop()
            solve(i+1,temp,result,k)

        result = []
        solve(0,[],result,k)
        return result