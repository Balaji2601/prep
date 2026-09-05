# https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

from collections import defaultdict

class Solution:
    def kosaraju(self, V, edges):
        def topo_DFS(adj, u, visited, stack):
            visited[u] = True
            
            for v in adj[u]:
                if not visited[v]:
                    topo_DFS(adj, v, visited, stack)
            
            stack.append(u)
        
        
        def DFS(adj, u, visited):
            visited[u] = True
            
            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, v, visited)
        
        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        
        # Step1: Do topological sort on adj
        stack = []
        visited = [False]*V
        for i in range(V):
            if not visited[i]:
                topo_DFS(adj, i, visited, stack)
                
        
        # Step2: Reverse the given directed edges
        reverse_adj = defaultdict(list)
        for u,v in edges:
            reverse_adj[v].append(u)
        
        # Step3: Do the DFS on the reverse_adj on the topo stack
        visited = [False]*V
        stack = stack[::-1]
        ans = 0
        for i in stack:
            if not visited[i]:
                DFS(reverse_adj, i, visited)
                ans += 1
        
        return ans
                