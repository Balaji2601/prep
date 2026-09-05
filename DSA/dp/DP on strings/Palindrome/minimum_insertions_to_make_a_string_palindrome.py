# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

# recursion + memoization
# the solve() is taken inspiration from edit_distance
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        def solve(i,j):
            if i >= j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = solve(i+1, j-1)
                return dp[i][j]
            else:
                insert_at_last = 1+solve(i+1,j)
                insert_at_first = 1+solve(i,j-1)
                return min(insert_at_last, insert_at_first)
        
        return solve(0,n-1)
    
# explanation
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        # dp[i][j] stores the minimum insertions needed
        # to make s[i:j+1] a palindrome
        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            # A single character or an empty substring
            # is already a palindrome
            if i >= j:
                return 0

            # If this substring was already solved,
            # return the stored answer
            if dp[i][j] != -1:
                return dp[i][j]

            # If characters at both ends are equal,
            # no insertion is needed for them.
            # Just solve the substring inside them.
            if s[i] == s[j]:
                dp[i][j] = solve(i + 1, j - 1)
                return dp[i][j]

            else:
                # Option 1: Insert s[i] at the end.
                # The inserted s[i] matches the original s[i], so the left character
                # s[i] is now handled and we move i forward.
                # s[j] is NOT handled yet—it did not get matched with its counterpart
                # from the original substring—so j stays where it is.
                # Therefore, solve the remaining substring s[i+1:j+1].
                insert_at_last = 1 + solve(i + 1, j)


                # Option 2: Insert s[j] at the beginning.
                # The inserted s[j] matches the original s[j], so the right character
                # s[j] is now handled and we move j backward.
                # s[i] is NOT handled yet—it did not get matched with its counterpart
                # from the original substring—so i stays where it is.
                # Therefore, solve the remaining substring s[i:j].
                insert_at_first = 1 + solve(i, j - 1)


                # Choose the option requiring fewer insertions
                dp[i][j] = min(insert_at_last, insert_at_first)

                return dp[i][j]

        # Find minimum insertions needed for the entire string
        return solve(0, n - 1)

# blue print
class Solution:
    def minInsertions(self, s:str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for L in range(1,n+1):
            for i in range(n-L+1):
                j = i+L-1
                if i == j:
                    dp[i][j] = 0
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i+1][j],dp[i][j-1])
        
        return dp[0][n-1]