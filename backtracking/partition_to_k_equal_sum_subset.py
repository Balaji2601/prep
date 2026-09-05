from typing import List

# Revise
# Fill bucket one after another using used/visited array
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        nums.sort(reverse = True)
        if total % k != 0:
            return False
        
        target = total//k
        # If target is 10 and max(nums) == 11 then we cannot fill k buckets with sum 10
        if max(nums) > target:
            return False
        used = [False]*n
        def solve(i,k,subSum):
            if k == 1:
                return True
            if subSum == target:
                return solve(0,k-1,0)
            
            for j in range(i,n):
                if used[j] or subSum + nums[j] > target:
                    continue
                
                used[j] = True
                if solve(j+1, k, subSum + nums[j]):
                    return True
                used[j] = False
            
            return False
        
        return solve(0,k,0)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False

        # each bucket sum == target 
        target = sum(nums)//k
        bucket = [0]*k
        nums.sort(reverse = True)

        def solve(i):
            if i == n:
                return True
            
            for j in range(k):
                if bucket[j] + nums[i] <= target:
                    bucket[j] += nums[i]
                    if solve(i+1):
                        return True
                    bucket[j] -= nums[i]

                    if bucket[j] == 0:
                        break

            return False
        
        return solve(0)