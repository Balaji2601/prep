# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

from functools import cache

class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)

        @cache
        def solve(i, target):
            # we are not returning when we reach target ie if target == 0
            # as the constraints include 0 as well so we go till end of every subset and check if target = 0 
            # if target is zero we return 1 as we found a way.
            if i == n:
                return 1 if target == 0 else 0

            pick = 0
            if arr[i] <= target:
                pick = solve(i + 1, target - arr[i])

            skip = solve(i + 1, target)

            return pick + skip

        return solve(0, target)
    

# without cache

class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = {}

        def solve(i, target):
            if i >= n:
                return 1 if target == 0 else 0

            if (i, target) in dp:
                return dp[(i, target)]

            pick = 0
            if arr[i] <= target:
                pick = solve(i + 1, target - arr[i])

            skip = solve(i + 1, target)

            dp[(i, target)] = pick + skip
            return dp[(i, target)]

        return solve(0, target)