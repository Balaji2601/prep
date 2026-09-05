# https://leetcode.com/problems/flood-fill/description/
# matrix

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m = len(image)
        n = len(image[0])
        def DFS(image, i, j, ic): # ic is initial colour
            def bound(i, j):
                if 0 <= i < m and 0 <= j < n and image[i][j] == ic:
                    return True
                return False
            image[i][j] = color

            for di,dj in directions:
                ni = i + di
                nj = j + dj

                if bound(ni, nj):
                    DFS(image, ni, nj, ic)

        initial_color = image[sr][sc]
        if initial_color == color:
            return image
        
        DFS(image, sr, sc, initial_color)
        return image