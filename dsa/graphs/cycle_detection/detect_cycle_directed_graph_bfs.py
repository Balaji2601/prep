# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from collections import defaultdict, deque

class Solution:
    def isCyclic(self, V, edges):
        # code here
        adj = defaultdict(list)
        in_degree = [0]*V
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        que = deque([])
        
        for i in range(V):
            if in_degree[i] == 0:
                que.append(i)
        
        count = 0
        while que:
            u = que.popleft()
            count += 1
            
            for v in adj[u]:
                in_degree[v] -= 1
                
                if in_degree[v] == 0:
                    que.append(v)
        
        if count != V:
            return True
        return False