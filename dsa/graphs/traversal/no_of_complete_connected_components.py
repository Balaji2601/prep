# https://leetcode.com/problems/count-the-number-of-complete-components/description/

from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(adj, u, visited, values):
            visited[u] = True
            values[0] += len(adj[u])
            values[1] += 1

            for v in adj[u]:
                if not visited[v]:
                    dfs(adj, v, visited, values)

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                values = [0, 0]
                dfs(adj, i, visited, values)
                # values[0] -> no of edges in this component
                # values[1] -> no of vertices in this component
                values[0] = values[0] // 2
                values[1] = (values[1]) * (values[1] - 1) // 2

                if values[0] == values[1]:
                    count += 1

        return count
