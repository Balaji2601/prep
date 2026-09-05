# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[-1])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        search = []
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    search.append((i,j))
        

        def bound(i,j,in_recursion,idx):
            if 0<=i<m and 0<=j<n and in_recursion[i][j] == False and word[idx] == board[i][j]:
                return True
            return False

        def dfs(i,j,in_recursion,idx):
            if idx+1 == len(word):
                return True

            in_recursion[i][j] = True

            for di,dj in directions:
                ni = i+di
                nj = j+dj

                if bound(ni,nj, in_recursion,idx+1):
                    if dfs(ni,nj,in_recursion,idx+1):
                        return True
            
            in_recursion[i][j] = False
            return False



        for i,j in search:
            in_recursion = [[False]*n for _ in range(m)]
            if dfs(i,j,in_recursion,0):
                return True
        
        return False
                

