# https://leetcode.com/problems/valid-parentheses/

# Revise
class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}":"{", "]":"[", ")": "("}
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] not in d:
                stack.append(s[i])
            else:
                if stack and d[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return stack == []
