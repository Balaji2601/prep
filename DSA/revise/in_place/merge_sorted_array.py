# https://leetcode.com/problems/merge-sorted-array/description

from typing import List

# Revise
# in place idx magic
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        for j in range(n):
            nums1[i] = nums2[j]
            i += 1
        nums1.sort()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()

# O(m+n) 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        ans = [0]*(m+n)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans[k] = nums1[i]
                i += 1
            else:
                ans[k] = nums2[j]
                j += 1
            k += 1
        if j < n:
            ans = ans[:k]+nums2[j:]
        if i < m:
            ans = ans[:k]+nums1[i:]
        for i in range(m+n):
            nums1[i] = ans[i]