# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from collections import defaultdict

class Solution:
    def DFS(self, adj, u, visited, in_recursion):
        visited[u] = True
        in_recursion[u] = True

        for v in adj[u]:
            if not visited[v]:
                cycle_detected = self.DFS(adj, v, visited, in_recursion)
                if cycle_detected:
                    return True
            elif in_recursion[v]:
                return True

        in_recursion[u] = False
        return False

    def is_cycle(self, V, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = [False]*V
        in_recursion = [False]*V

        # iterate through all graph components
        for i in range(V):
            if not visited[i]:
                cycle_detected = self.DFS(adj, i, visited, in_recursion)
                if cycle_detected:
                    return True

        return False
