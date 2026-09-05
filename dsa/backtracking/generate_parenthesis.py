# https://leetcode.com/problems/generate-parentheses/description/

from typing import List

# Revise
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def validate(arr):
            d = {")": "("}
            stack = []
            for i in range(len(arr)):
                if arr[i] not in d:
                    stack.append(arr[i])
                else:
                    if stack and stack[-1] == d[arr[i]]:
                        stack.pop()
                    else:
                        return False
            return stack == []

        N = n*2
        d = {"(": 0, ")": 0}
        p = "()"
        def solve(N, temp,result):
            if N == 0:
                if validate(temp):
                    result.append("".join(temp[:]))
                return
            
            for i in range(2):
                if d[p[i]] > n:
                    continue
                d[p[i]] += 1
                temp.append(p[i])
                solve(N-1, temp, result)
                temp.pop()
                d[p[i]] -= 1

        result = []
        solve(N, [], result)
        return result