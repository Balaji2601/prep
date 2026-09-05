# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from collections import defaultdict, deque

class Solution:
    def BFS(self, adj, u, visited, result):
        result.append(u)
        visited[u] = True
        que = deque([])
        que.append(u)
        
        while len(que) != 0:
            u = que.popleft()
            for v in adj[u]:
                if visited[v] != True:
                    que.append(v)
                    visited[v] = True
                    result.append(v)
            
    def bfs_on_graph(self, mp):
        V = len(mp) # no of vertices
        adj = defaultdict(list) # build adjacency graph
        
        for u in range(V):
            for v in mp[u]:
                adj[u].append(v)
        
        result = []
        visited = [False]*V
        self.BFS(adj, 0, visited, result)
        
        return result


if __name__ == "__main__":
    solution = Solution()
    mp = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(solution.bfs_on_graph(mp)) # [0, 2, 3, 1, 4]