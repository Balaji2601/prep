# https://leetcode.com/problems/unique-paths/description

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        # solve(i,j) gives no of unique paths from (i,j) cell to (m-1,n-1) cell
        # at (i,j) we can go to either (i+1,j) down or (i,j+1) right
        # so unique paths from (i,j) to (m-1,n-1) is sum(unique_paths_from (i+1,j) to (m-1,n-1), unique_paths_from (i,j+1) to (m-1,n-1))
        def solve(i,j):
            # here we will not go to i < 0 or j < 0 because we are moving right and down 
            # if we move in all directions(up, right, down, left) and diagonals we include like this
            # if i < 0 or i >= m or j < 0 or j >= m
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            right = solve(i,j+1)
            down = solve(i+1,j) 

            dp[i][j] = right+down
            return dp[i][j]
        
        # so if we call solve with (i,j) = (0,0) we are going to (m-1,n-1) cell from (0,0)
        # and solve(0,0) returns unique paths to (m-1, n-1) from (0,0)
        return solve(0,0)

# bottom up
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] represents no of unique paths to cell (i,j) from (0,0)
        dp = [[0]*n for _ in range(m)]
        # get to (0,0) from (0,0) is 1 path
        dp[0][0] = 1
        def bound(i,j):
            if 0<=i<m and 0<=j<n:
                return True
            return False

        # iterating through each (i,j)
        # to come to cell (i,j) we can only come from (i-1,j) or (i,j-1) meaning from up cell or from left cell to cell (i,j)
        # checking bound at each cell
        # this below iteration populates dp array.
        # by returning dp[m-1][n-1] gives us no of unique paths from (0,0) to (m-1,n-1).
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    if bound(i-1,j):
                        dp[i][j] += dp[i-1][j]
                    if bound(i,j-1):
                        dp[i][j] += dp[i][j-1]
        
        return dp[m-1][n-1]

# bottom up
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] represents no of unique paths to cell (i,j) from (0,0)
        dp = [[0]*n for _ in range(m)]
        """
        get to (0,0) from (0,0) is a path or 0
        it depends on the interviewer
        if it is 0 then above solution will be invalid for m,n == 1,1
        but if we include a if condition m,n == 1,1 then return 0 it will be valid
        in leetcode it is given as 1, so dp[0][0] = 1 
        or else if interviewer says dp[0][0] = 0 then below line
        """
        dp[0][0] = 1
        
        # for 1st row cells to reach unique path is 1
        for j in range(n):
            dp[0][j] = 1
        # for 1st column cells to reach unique path is 1
        for i in range(m):
            dp[i][0] = 1

        # as we calculated for 1st row and column
        # we are starting from 2nd row and 2nd column
        # and out of bound is not a case in here for i-1, j-1 as i-1, j-1 is out of bound
        # for i,j = 0,0 only for Solution2
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]