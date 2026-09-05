# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
# https://www.youtube.com/watch?v=TGzyArbMu7w&list=PLpIkg8OmuX-JhFpkhgrAwZRtukO0SkwAt&index=37

# Fractional knapsack is a greedy approach not dp.
# greedy
# TC: O(nlogn)
# SC: O(n)
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        n = len(val)
        profit_per_unit = [0]*n
        for i in range(n):
            profit_per_unit[i] = (val[i], wt[i])
        
        # descending order of profit_per_unit means maximum to minimum
        profit_per_unit.sort(key = lambda x: -x[0]/x[1])
        
        ans = 0
        for i in range(n):
            curr_val, curr_wt = profit_per_unit[i]
            if curr_wt <= capacity:
                ans += curr_val
                capacity -= curr_wt
            else:
                ans += (curr_val/curr_wt) * capacity
                break
        
        return ans
