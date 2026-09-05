# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/

from collections import defaultdict
from typing import List

# DFS
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def DFS(adj, u, visited, no_of_vertices):
            visited[u] = True
            no_of_vertices[0] += 1

            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, v, visited, no_of_vertices)
            

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*n
        vertices_in_comp_count = []
        ans = 0
        for i in range(n):
            if not visited[i]:
                no_of_vertices = [0]
                DFS(adj, i, visited, no_of_vertices)
                V = no_of_vertices[0]
                ans += (n-V)*V
        
        return ans//2

