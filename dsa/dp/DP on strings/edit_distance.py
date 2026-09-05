# https://leetcode.com/problems/edit-distance/description/

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        def solve(i,j):
            if i >= n1:
                return n2-j
            if j >= n2:
                return n1-i

            if word1[i] == word2[j]:
                return solve(i+1,j+1)
            else:
                insert_operation = 1+solve(i,j+1)
                delete_operation = 1+solve(i+1,j)
                replace_operation = 1+solve(i+1,j+1)
            return min(insert_operation, delete_operation, replace_operation)

        return solve(0,0)

# recursion + memoization
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [[-1]*(n2+1) for _ in range(n1+1)]

        def solve(i,j):
            if i >= n1:
                return n2-j
            if j >= n2:
                return n1-i
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = solve(i+1,j+1)
                return solve(i+1,j+1)
            else:
                insert_operation = 1+solve(i,j+1)
                delete_operation = 1+solve(i+1,j)
                replace_operation = 1+solve(i+1,j+1)
            
            dp[i][j] = min(insert_operation, delete_operation, replace_operation)
            return min(insert_operation, delete_operation, replace_operation)

        return solve(0,0)

# recursion + memoization with length 
# starting at n1, n2 length reducing length in recursion
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [[-1]*(n2+1) for _ in range(n1+1)]

        def solve(m,n):
            if m == 0 or n == 0:
                return m+n
            if dp[m][n] != -1:
                return dp[m][n]

            if word1[m-1] == word2[n-1]:
                dp[m][n] = solve(m-1,n-1)
                return solve(m-1,n-1)
            else:
                insert_operation = 1+solve(m,n-1)
                delete_operation = 1+solve(m-1,n)
                replace_operation = 1+solve(m-1,n-1)
            
            dp[m][n] = min(insert_operation, delete_operation, replace_operation)
            return min(insert_operation, delete_operation, replace_operation)
        
        return solve(n1,n2)

# recursion + memoization with explanation
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        # dp[i][j] = minimum operations required to convert
        # word1[i:] into word2[j:]
        #
        # -1 means this state has not been calculated yet.
        dp = [[-1]*(n2+1) for _ in range(n1+1)]

        def solve(i,j):
            # BASE CASE 1:
            # If we have processed all characters of word1,
            # the remaining characters of word2 must all be inserted.
            #
            # Example:
            # word1[i:] = ""
            # word2[j:] = "abc"
            #
            # We need 3 insertions -> n2 - j
            if i >= n1:
                return n2-j

            # BASE CASE 2:
            # If we have processed all characters of word2,
            # the remaining characters of word1 must all be deleted.
            #
            # Example:
            # word1[i:] = "abc"
            # word2[j:] = ""
            #
            # We need 3 deletions -> n1 - i
            if j >= n2:
                return n1-i

            # If this state was already calculated,
            # return the stored result instead of recalculating it.
            if dp[i][j] != -1:
                return dp[i][j]

            # If the current characters are already equal,
            # no operation is needed.
            #
            # Both characters are matched, so move both
            # pointers to the next characters.
            if word1[i] == word2[j]:
                dp[i][j] = solve(i+1,j+1)
                return solve(i+1,j+1)

            else:
                # 1. INSERT:
                #
                # Insert word2[j] into word1 at i-1
                #
                # The inserted character matches word2[j],
                # so word2[j] has now been handled.
                # Therefore, move j forward.
                #
                # We did NOT remove or process word1[i].
                # word1[i] still needs to be handled,
                # so i stays at the same position.
                #
                # Cost of insertion = 1
                # Remaining problem = solve(i, j+1)
                insert_operation = 1+solve(i,j+1)

                # 2. DELETE:
                #
                # Delete the current character word1[i].
                #
                # Since word1[i] is deleted, we no longer
                # need to process it. Therefore, move i forward.
                #
                # We have NOT matched word2[j] yet,
                # so j stays at the same position.
                #
                # Cost of deletion = 1
                # Remaining problem = solve(i+1, j)
                delete_operation = 1+solve(i+1,j)

                # 3. REPLACE:
                #
                # Replace word1[i] with word2[j].
                #
                # After replacement, word1[i] becomes equal
                # to word2[j], so both characters are handled.
                # Therefore, move both i and j forward.
                #
                # Cost of replacement = 1
                # Remaining problem = solve(i+1, j+1)
                replace_operation = 1+solve(i+1,j+1)
            
            # Try all three operations and store the minimum
            # number of operations required.
            dp[i][j] = min(insert_operation, delete_operation, replace_operation)

            return min(insert_operation, delete_operation, replace_operation)

        # Start from the first character of both words.
        return solve(0,0)

class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(0, n1+1):
            for j in range(0, n2+1):
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # min(cost of operation + insert, cost of operation + replace, cost of operation + delete)
                    dp[i][j] = min(1+dp[i][j-1], 1+dp[i-1][j-1], 1+dp[i-1][j])
        
        return dp[n1][n2]