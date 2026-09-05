# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        dp = [[None]*(W+1) for _ in range(n+1)]
        def solve(idx, W):
            if idx >= n or W == 0:
                return 0

            if dp[idx][W] is not None:
                return dp[idx][W]
            
            pick = 0
            if wt[idx] <= W:
                pick = val[idx] + solve(idx+1, W-wt[idx])
            
            skip = solve(idx+1, W)
            dp[idx][W] = max(skip, pick)
            return dp[idx][W]
            
        return solve(0, W)

class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        # solve(n, W) = maximum profit using the first n items
        # with knapsack capacity W
        def solve(n,W):
            # profit you get when there are no items left(n = 0) or there is no place(W=0) to fill knapsack is zero
            if n == 0 or W == 0:
                return 0
            
            # you want to pick up item at n-1 idx
            # you can only pick this item if 
            # say n-1th item weight 6 and weight left to fill knapsack is 5
            # then you cannot pick this item weight 6
            # so to pick this we need n-1 item weight should be either 5 or less than it
            pick = 0
            if wt[n-1] <= W:
                # now you picked the item so val is added to the profit
                # and the length of the picking will be n-1 right
                # and weight of knapsack is reduced to W-wt[n-1]
                pick = val[n-1]+solve(n-1,W-wt[n-1])
            
            skip = solve(n-1, W)

            return max(skip, pick)

        return solve(n,W)
    

class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        # dp[i][j] = maximum profit we can get using the first i items with a knapsack capacity of j
        dp = [[0]*(W+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1, W+1):
                take = 0
                if wt[i-1] <= j:
                    take = val[i-1] + dp[i-1][j-wt[i-1]]
                skip = dp[i-1][j]

                dp[i][j] = max(take, skip)
        
        # maximum profit we get using first n items with a knapsack capacity W
        return dp[n][W]