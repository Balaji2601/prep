# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, V: int, mp: List[List[int]]) -> bool:
        def isCycleDFS(adj, u, visited, in_recursion):
            visited[u] = True
            in_recursion[u] = True

            for v in adj[u]:
                if not visited[v]:
                    is_cycle = isCycleDFS(adj, v, visited, in_recursion)
                    if is_cycle:
                        return True
                elif in_recursion[v]:
                    return True
            
            in_recursion[u] = False
            return False

        adj = defaultdict(list)
        for u, v in mp:
            adj[v].append(u)
        
        visited = [False]*V
        in_recursion = [False]*V

        for i in range(V):
            if not visited[i] and isCycleDFS(adj, i, visited, in_recursion):
                return False
        return True