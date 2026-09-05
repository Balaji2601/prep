# https://leetcode.com/problems/longest-string-chain/description/

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        # sort by length of each word
        words.sort(key = lambda x:len(x))
        
        def check(a,b):
            i = 0
            m = len(b)
            while i < m:
                if a == b[:i] + b[i+1:]:
                    return True
                i += 1
            return False

        dp = [[-1]*(n+1) for _ in range(n+1)]
        def solve(i, prev):
            if i >= n:
                return 0
            
            if prev != -1 and dp[i][prev] != -1:
                return dp[i][prev]

            choose = 0
            if prev == -1 or (len(words[prev]) + 1 == len(words[i]) and check(words[prev], words[i])):
                choose = 1+solve(i+1,i)
            
            skip = solve(i+1,prev)

            if prev != -1:
                dp[i][prev] = max(choose,skip)
            return max(choose,skip)



        return solve(0, -1) # curr, prev


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        # sort by length of each word
        words.sort(key = lambda x:len(x))

        def check(a,b):
            i = 0
            m = len(b)
            while i < m:
                if a == b[:i] + b[i+1:]:
                    return True
                i += 1
            return False

        dp = [1]*n

        ans = 1

        for i in range(n):
            for j in range(i):
                if len(words[j])+1 == len(words[i]) and check(words[j], words[i]):
                    dp[i] = max(1+dp[j], dp[i])
                    ans = max(ans, dp[i])

        return ans