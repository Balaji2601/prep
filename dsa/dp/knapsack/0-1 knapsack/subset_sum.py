# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

class Solution:
    def isSubsetSum(self, arr: list[int], W: int) -> bool:
        # code here
        n = len(arr)
        dp = {}
        def solve(n,W):
            if W == 0:
                return True
            if n == 0 or W < 0:
                return False
            
            if (n,W) in dp:
                return dp[(n,W)]

            # if we find a true anywhere we return it instantly
            if solve(n-1,W-arr[n-1]):
                dp[(n,W)] = True
                return True
            
            if solve(n-1,W):
                dp[(n,W)] = True
                return True
            
            dp[(n,W)] = False
            return False

        return solve(n,W)