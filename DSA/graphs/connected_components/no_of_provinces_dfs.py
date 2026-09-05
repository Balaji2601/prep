# https://leetcode.com/problems/number-of-provinces/description/
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def DFS(isConnected, u, visited, n):
            if visited[u]:
                return
            
            visited[u] = True

            for v in range(n):
                if isConnected[u][v]:
                    DFS(isConnected, v, visited, n)


        V = len(isConnected)
        visited = [False]*V
        count = 0
        for i in range(V):
            if not visited[i]:
                DFS(isConnected, i, visited, V)
                count += 1
        return count

from collections import defaultdict

class Solution2:
    def DFS(self, adj, u, visited):
        if visited[u]:
            return
        visited[u] = True
        for v in adj[u]:
            self.DFS(adj, v, visited)

    def findCircleNum(self, mp: List[List[int]]) -> int:
        adj = defaultdict(list)
        V = len(mp)
        for u in range(1,V+1):
            for v in range(1,V+1):
                if u == v:
                    continue
                if mp[u-1][v-1]: 
                    adj[u].append(v)
        
        visited = [False]*(V+1)
        count = 0
        for i in range(1, V+1):
            if not visited[i]:
                count += 1
            self.DFS(adj, i, visited)
        return count