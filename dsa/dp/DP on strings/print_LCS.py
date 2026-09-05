# https://leetcode.com/problems/longest-common-subsequence/description/

# print


class Solution:
    def print_longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(0, m+1):
            for j in range(0, n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        ans = ""
        i = m
        j = n

        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                ans += text1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        print(ans[::-1])

        return dp[m][n]

class Solution:
    def print_longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[i][j] = length of the Longest Common Subsequence
        # between text1[:i] and text2[:j]
        #
        # dp has an extra row and column to handle empty strings.
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(0, m+1):
            for j in range(0, n+1):
                # BASE CASE:
                # If either string prefix is empty, there cannot
                # be any common subsequence.
                #
                # Example:
                # LCS("", "abc") = 0
                # LCS("abc", "") = 0
                #
                # Therefore:
                # dp[0][j] = 0 for every j
                # dp[i][0] = 0 for every i
                if i == 0 or j == 0:
                    dp[i][j] = 0
                # If the current characters match,
                # include this character in the LCS.
                #
                # Move diagonally because both characters
                # are now considered.
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                # Characters don't match, so we cannot
                # include both in the common subsequence.
                #
                # Two choices:
                #
                # 1. Skip text1[i-1]
                #    -> dp[i-1][j]
                #
                # 2. Skip text2[j-1]
                #    -> dp[i][j-1]
                #
                # Take the option with the longer LCS.
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        ans = ""
        i = m
        j = n

        while i > 0 and j > 0:
            # If characters match, this character belongs to the LCS.
            #
            # Add it and move diagonally because both characters
            # have been used.
            if text1[i-1] == text2[j-1]:
                ans += text1[i-1]
                i -= 1
                j -= 1
            else:
                # Characters don't match.
                #
                # Move in the direction that preserves
                # the longer LCS.
                #
                # dp[i-1][j] -> skip character from text1
                # dp[i][j-1] -> skip character from text2
                if dp[i-1][j] > dp[i][j-1]:
                    # LCS is longer by skipping text1[i-1]
                    i -= 1
                else:
                    # LCS is longer (or equal) by skipping text2[j-1]
                    j -= 1
        
        # Since we started from the end of both strings,
        # characters were added to ans in reverse order.
        #
        # So reverse ans to get the actual LCS.
        print(ans[::-1])

        return dp[m][n]