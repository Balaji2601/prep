# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List

# Revise
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        for r in range(n):
            if r == 0:
                continue
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l+1
