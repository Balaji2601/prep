# https://leetcode.com/problems/longest-increasing-subsequence/description/

from bisect import bisect_left
from typing import List

# We can print LIS using this patience sorting algorithm

class Solution:
    def longestLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = []

        # O(nlogn)
        for i in range(n):# O(n)
            # O(logn)
            index = bisect_left(ans, nums[i]) # index of element ie just greater than nums[i] in ans array

            # if index is out of bound of ans ie len(ans) we append nums[i] at last
            # meaning we found a bigger element than max(ans)
            if index == len(ans):
                ans.append(nums[i])
            # if we found index we update the ans[index] with nums[i]
            else:
                ans[index] = nums[i]

        return len(ans)