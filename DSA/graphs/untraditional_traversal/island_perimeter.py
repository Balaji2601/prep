# https://leetcode.com/problems/island-perimeter/
# matrix

class Solution:
    def islandPerimeter(self,grid):
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj

                        # This condition is basically, if there is a block add it to perimeter.
                        if ni >= rows or ni < 0 or nj >= cols or nj < 0 or grid[ni][nj] == 0:
                            perimeter += 1

        return perimeter

# Using DFS concept, but the code is not traditional
class Solution2:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def DFS(grid, i, j, visited):
            if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == 0:
                return 1
            if visited[i][j]:
                return 0

            visited[i][j] = True
            perimeter = 0
            for di, dj in directions:
                ni = i+di
                nj = j+dj
                perimeter += DFS(grid, ni, nj, visited)

            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    perimeter = DFS(grid, i, j, visited)
                    return perimeter

        
    
if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    grid = [[1,1],[1,1]]
    print(Solution().islandPerimeter(grid))
    print(Solution2().islandPerimeter(grid))