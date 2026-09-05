# https://leetcode.com/problems/shortest-common-supersequence/description/

# print

class Solution:
    def print_SCS(self, str1, str2):
        m = len(str1)
        n = len(str2)

        # dp[i][j] = length of the shortest common supersequence
        # formed using:
        # str1 till length i and 
        # str2 till length j
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(0,m+1):
            for j in range(0,n+1):
                # If one string is empty, we must include
                # all characters of the other string
                #
                # Example:
                # SCS("abc", "") = "abc" -> length 3
                # SCS("", "xyz") = "xyz" -> length 3
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                # If the current characters are the same,
                # include that character only ONCE
                #
                # Then solve for the remaining prefixes
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                # If characters are different, we have two choices:
                #
                # 1. Include str1[i-1] and solve dp[i-1][j]
                # 2. Include str2[j-1] and solve dp[i][j-1]
                #
                # Choose the option producing the shorter SCS
                else:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1])
        
        i = m
        j = n
        ans = ""
        while i > 0 and j > 0:
            # Same character in both strings
            # Include it only once and move diagonally
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i -= 1
                j -= 1
            else:
                # Check which previous state was used
                # to create the shorter SCS
                #
                # dp[i-1][j] means:
                # take str1[i-1]
                #
                # dp[i][j-1] means:
                # take str2[j-1]
                if dp[i-1][j] < dp[i][j-1]:
                    # Taking str1[i-1] gives a shorter path
                    ans += str1[i-1]
                    i -= 1
                
                else:
                    # Taking str2[j-1] gives a shorter/equal path
                    ans += str2[j-1]
                    j -= 1
        
        # If str2 is exhausted, append remaining characters of str1
        while i > 0:
            ans += str1[i-1]
            i -= 1
        # If str1 is exhausted, append remaining characters of str2
        while j > 0:
            ans += str2[j-1]
            j -= 1
        
        # We constructed the answer backwards,
        # so reverse it before returning
        return ans[::-1]

            
