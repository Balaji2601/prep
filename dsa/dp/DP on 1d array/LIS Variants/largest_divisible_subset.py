# https://leetcode.com/problems/largest-divisible-subset/description/

# print

from typing import List

# recursion + memoization
# with passing previous value
# backtracking
class Solution1:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # sort in ascending order
        nums.sort()
        def solve(curr_idx, prev_val, temp, result):
            if curr_idx >= n:
                if len(temp) > len(result):
                    result[:] = temp[:]
                return
            
            if prev_val == -1 or nums[curr_idx] % prev_val == 0:
                temp.append(nums[curr_idx])
                # choose
                solve(curr_idx+1, nums[curr_idx], temp, result)
                temp.pop()
            
            # skip
            solve(curr_idx+1, prev_val, temp, result)


        temp = []
        result = []
        
        solve(0, -1, temp, result)

        return result

# recursion + memoization
# with passing previous idx
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        def solve(curr_idx, prev_idx, temp, result):
            if curr_idx >= n:
                if len(temp) > len(result):
                    result[:] = temp[:]
                return
            
            if prev_idx == -1 or nums[curr_idx] % nums[prev_idx] == 0:
                temp.append(nums[curr_idx])
                # choose
                solve(curr_idx+1, curr_idx, temp, result)
                temp.pop()
            
            # skip
            solve(curr_idx+1, prev_idx, temp, result)


        temp = []
        result = []
        
        solve(0, -1, temp, result)
        return result

class Solution2:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # sort in ascending order
        nums.sort()
        n = len(nums)
        dp = [1]*n
        prev_idx = [-1]*n
        last_chosen_idx = 0
        maxL = 1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1 
                        # dp[i] = max(dp[i], dp[j]+1) line 16 and line 17 both are same because of line 15 if condition.
                        prev_idx[i] = j
                
        
        len_of_largest_subset = max(dp)

        for i in range(n-1, -1, -1):
            if dp[i] == len_of_largest_subset:
                last_chosen_idx = i
                break
        
        ans = []
        while last_chosen_idx != -1:
            ans.append(nums[last_chosen_idx])
            last_chosen_idx = prev_idx[last_chosen_idx]
        
        return ans

# calculating last chosen index in the first for loop itself.
class Solution3:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1]*n
        prev_idx = [-1]*n
        last_chosen_idx = 0
        maxL = 1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        prev_idx[i] = j

                    if maxL < dp[i]:
                        maxL = dp[i]
                        last_chosen_idx = i
        
        ans = []
        while last_chosen_idx != -1:
            ans.append(nums[last_chosen_idx])
            last_chosen_idx = prev_idx[last_chosen_idx]
        
        return ans



