from collections import defaultdict, deque

class Solution:
    def TreeDiameter(V, edges):
        def bfs(adj, src):
            visited = [False]*V
            visited[src] = True
            level = 0
            farthest_node = src

            q = deque([src])

            while q:
                size = len(q)
                for _ in range(size):
                    u = q.popleft()
                    farthest_node = u

                    for v in adj[u]:
                        if not visited[v]:
                            q.append(v)
                if q:
                    level += 1

            return farthest_node, level

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        farthest_node, level = bfs(adj, 0) # 0 is node where the bfs is starting from

        _, diameter = bfs(adj, farthest_node)

        return diameter




