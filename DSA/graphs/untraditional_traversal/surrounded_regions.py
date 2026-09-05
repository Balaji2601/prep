# https://leetcode.com/problems/surrounded-regions/description/
# matrix

from typing import List

# Traversing dfs from the top row, bottom row, leftmost column, rightmost column of the board
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bound(i, j, visited):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and board[i][j] == "O":
                return True
            return False

        def dfs(i, j, visited):
            visited[i][j] = True

            for di, dj in directions:
                ni = i+di
                nj = j+dj
                if bound(ni, nj, visited):
                    dfs(ni, nj, visited)

        for i in range(m):
            if board[i][0] == "O": 
                dfs(i, 0, visited) # DFS from extreme left column
            if board[i][n-1] == "O":
                dfs(i, n-1, visited) # DFS from exterme right column
    
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j, visited) # DFS from extreme top row
            
            if board[m-1][j] == "O":
                dfs(m-1, j, visited) # DFS from extreme bottom row

        # in the visited array the true values are which we traverse from extremes "O" to inside 
        # other "O"s which are not connected to extremes will be false and in the below for loop 
        # we change the board "O"s to "X" 
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False:
                    board[i][j] = "X"


