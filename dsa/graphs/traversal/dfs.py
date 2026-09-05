# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

from collections import defaultdict

class Solution:
    def DFS(self, adj, u, visited, result):
        if visited[u] == True:
            return

        visited[u] = True
        result.append(u)

        for v in adj[u]:
            if visited[v] != True:
                self.DFS(adj, v, visited, result)
        

    def dfs_on_graph(self, mp): # mp means map
        # convert mp to adjacency list
        V = len(mp) # length of vertices
        adj = defaultdict(list) # build graph

        for u in range(V):
            for v in mp[u]:
                adj[u].append(v)

        visited = [False]*V
        result = []

        self.DFS(adj, 0, visited, result)

        return result
        

if __name__ == "__main__":
    solution = Solution()
    mp = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(solution.dfs_on_graph(mp)) # [0, 2, 4, 3, 1]