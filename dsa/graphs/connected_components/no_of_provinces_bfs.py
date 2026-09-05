# https://leetcode.com/problems/number-of-provinces/description/
from collections import defaultdict, deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def BFS(adj, u, visited):
            visited[u] = True

            que = deque([])
            que.append(u)

            while que:
                u = que.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        que.append(v)
                        visited[v] = True
                    
        V = len(isConnected)
        adj = defaultdict(list)

        for u in range(V):
            for v in range(V):
                if isConnected[u][v]:
                    adj[u].append(v)
                    adj[v].append(u)
        
        visited = [False]*V

        count = 0
        for i in range(V):
            if not visited[i]:
                BFS(adj, i, visited)
                count += 1
        
        return count