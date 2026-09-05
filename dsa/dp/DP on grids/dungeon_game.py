# https://leetcode.com/problems/dungeon-game/description

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[-1]*n for _ in range(m)]
        # solve(i,j) returns minimum health points required 
        # if the knight go from (i,j) to (m-1,n-1)
        def solve(i,j):
            if i >= m or j >= n:
                return float("inf")
            """
            Base Case: Minimum HP required for knight to go (m-1,n-1) from (m-1,n-1) cell is
            say value of (m-1,n-1) is -6. To tackle this cell knight should have minimum of 7 HP 
            ie abs(dungeon[i][j])+1 if dungeon[i][j] < 0 else 1 HP is required
            """
            if i == m-1 and j == n-1:
                if dungeon[i][j] > 0:
                    return 1
                elif dungeon[i][j] < 0:
                    return abs(dungeon[i][j])+1
                else:
                    return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            right = solve(i,j+1)
            down = solve(i+1,j)

            """
            right = Minimum HP required to go from the right cell to the destination.
            down = Minimum HP required to go from the down cell to the destination.

            The knight should choose the path requiring minimum HP:
                min(right, down)

            This is the HP we need AFTER dealing with the current cell.

            But we need to know the HP required BEFORE entering the current cell.
            Therefore, we reverse the effect of the current cell:

            - If dungeon[i][j] is positive, the cell gives us HP,
              so we need less HP before entering:
                  "required HP" = next requirement - positive value

            - If dungeon[i][j] is negative, the cell takes away HP,
              so we need more HP before entering:
                  "required HP" = next requirement - negative value

            Therefore:
                hp_needed_before_effect = minimum HP needed after current cell
                         - HP gained/lost in current cell
            """

            hp_needed_before_effect = min(right,down)-dungeon[i][j]

            """
            If hp_needed_before_effect <= 0:
                This cell's heal already covers everything the rest of the path
                needs — the knight could enter with 0 or negative HP and still
                survive downstream. But HP can never be <= 0 at any cell, so we
                still require the bare minimum: 1.

            If hp_needed_before_effect > 0:
                This cell's heal (if any) isn't enough to cover the rest of the
                path's requirement — the knight must enter with exactly
                hp_needed_before_effect HP, or he won't survive to the end.

            So dp[i][j] is always max(hp_needed_before_effect, 1) — the true
            minimum HP needed to enter this cell and survive to the princess.
            """
            dp[i][j] = hp_needed_before_effect if hp_needed_before_effect > 0 else 1
            return dp[i][j]
        
        return solve(0,0)
