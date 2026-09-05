# https://leetcode.com/problems/remove-element/description/

from typing import List

# Revise
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k