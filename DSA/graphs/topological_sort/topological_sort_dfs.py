# https://www.geeksforgeeks.org/problems/topological-sort/1

from collections import defaultdict

class Solution:
    def DFS(self, adj, u, visited, stack):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.DFS(adj, v, visited, stack)
        stack.append(u)
        
    def topoSort(self, V, edges):
        # Code here
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        visited = [False]*V
        stack = []
        
        for i in range(V):
            if not visited[i]:
                self.DFS(adj, i, visited, stack)
        
        ans = []
        while stack:
            ans.append(stack.pop())
        
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.topoSort(V = 4, edges= [[3, 0], [1, 0], [2, 0]]))