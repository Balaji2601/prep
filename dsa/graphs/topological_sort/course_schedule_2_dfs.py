# https://leetcode.com/problems/course-schedule-ii/submissions/2086880787/

from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, V: int, mp: List[List[int]]) -> List[int]:
        def DFS(adj, u, visited, in_recursion, stack):
            visited[u] = True
            in_recursion[u] = True

            for v in adj[u]:
                if not visited[v]:
                    is_cycle = DFS(adj, v, visited, in_recursion, stack)
                    if is_cycle:
                        return True
                elif in_recursion[v]:
                    return True

            in_recursion[u] = False
            stack.append(u)
            return False
        
        adj = defaultdict(list)

        for u,v in mp:
            adj[v].append(u)
        
        visited = [False]*V
        in_recursion = [False]*V
        stack = []
        
        for i in range(V):
            if not visited[i]:
                is_cycle = DFS(adj, i, visited, in_recursion, stack)
                if is_cycle:
                    return []

        return stack[::-1]