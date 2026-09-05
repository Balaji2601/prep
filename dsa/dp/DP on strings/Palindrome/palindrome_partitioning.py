# https://leetcode.com/problems/palindrome-partitioning/description/

# print

from typing import List

# DP + Backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for L in range(1,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp[i][j] = True
                elif i+1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        
        result = []
        def solve(i,partition):
            if i >= n:
                result.append(partition[:])
                return
            
            # O(2**n)
            for j in range(i,n):
                # if substring s[i:j+1] is palindrome then only we will be doing partitioning
                if dp[i][j] == True: # O(1) as we already calculated above
                    partition.append(s[i:j+1])
                    # Since indices i through j are already included in the
                    # current partition, start the next partition from j+1.
                    #
                    # Example: s = "abac", i = 0, j = 2
                    # We choose "aba", which covers indices 0, 1, and 2.
                    #
                    # "a b a c"
                    #  └───┘
                    #   "aba"
                    #
                    # So the next unprocessed character starts at index 3,
                    # which is j + 1.
                    solve(j+1,partition)
                    partition.pop()

        solve(0,[])
        return result

# Backtracking
# Without optimization of palindrome check
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        result = []
        def solve(i,partition):
            if i >= n:
                result.append(partition[:])
                return
            
            # O(2**n)
            for j in range(i,n):
                # if substring s[i:j+1] is palindrome then only we will be doing partitioning
                # after partitioning i moves to j+1 for the next recursion
                # Eg: "abac" at start i = 0 and j = 2 we do the partitioning then i moves to j+1
                # For understanding skipped 1 length "a" substring
                if s[i:j+1] == s[i:j+1][::-1]: # O(n)
                    partition.append(s[i:j+1])
                    # Since indices i through j are already included in the
                    # current partition, start the next partition from j+1.
                    #
                    # Example: s = "abac", i = 0, j = 2
                    # We choose "aba", which covers indices 0, 1, and 2.
                    #
                    # "a b a c"
                    #  └───┘
                    #   "aba"
                    #
                    # So the next unprocessed character starts at index 3,
                    # which is j + 1.
                    solve(j+1,partition)
                    partition.pop()

        solve(0,[])
        return result