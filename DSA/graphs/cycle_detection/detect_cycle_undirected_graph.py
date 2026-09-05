# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from collections import defaultdict, deque

class Solution:
    def DFS(self, adj, u, visited, parent):
        visited[u] = True

        for v in adj[u]:
            if v == parent:
                continue

            if visited[v]:
                return True

            if self.DFS(adj, v, visited, u):
                return True

        return False

    def BFS(self, adj, u, visited, parent):
        visited[u] = True
        que = deque([])
        que.append((u, parent))

        while que:
            u, parent = que.popleft()
            for v in adj[u]:
                if v == parent:
                    continue
                if visited[v] == True:
                    return True
                visited[v] = True
                que.append((v, u))

        return False

    def is_cycle_undirected(self, V, edges, solve_in_DFS):
        adj = defaultdict(list)
        for u,v in edges:
            # for undirected graph
            adj[u].append(v) 
            adj[v].append(u)

        visited = [False]*V

        for i in range(V):
            if solve_in_DFS:
                if not visited[i]:
                    if self.DFS(adj, i, visited, -1):
                        return True
            else:
                if not visited[i]:
                    if self.BFS(adj, i, visited, -1):
                        return True
        return False
        

if __name__ == "__main__":
    V = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    s = Solution()
    print(s.is_cycle_undirected(V, edges, True))