# https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1

# With lexicographical order

from collections import defaultdict
import heapq as hq

class Solution:
    def shortestPath(self, V, edges, src, dest):
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        # Sort neighbors to help process smaller vertices first
        for u in adj:
            adj[u].sort()

        dist = [float("inf")] * (V + 1)
        path = [[] for _ in range(V + 1)]

        dist[src] = 0
        path[src] = [src]

        pq = [(0, src)]

        while pq:
            d, u = hq.heappop(pq)

            if d > dist[u]:
                continue

            for v, wt in adj[u]:
                new_dist = d + wt
                new_path = path[u] + [v]

                # Shorter path found
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    path[v] = new_path
                    hq.heappush(pq, (new_dist, v))

                # Same distance but lexicographically smaller path
                elif new_dist == dist[v] and new_path < path[v]:
                    path[v] = new_path
                    hq.heappush(pq, (new_dist, v))

        if dist[dest] == float("inf"):
            return [-1]

        return path[dest]


# Without lexicographic order

class Solution2:
    def shortestPath(self, V, edges, src, dest):
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        dist = [float("inf")] * (V + 1)
        path = [[] for _ in range(V + 1)]

        dist[src] = 0
        path[src] = [src]

        pq = [(0, src)]

        while pq:
            d, u = hq.heappop(pq)

            if d > dist[u]:
                continue

            for v, wt in adj[u]:
                new_dist = d + wt
                new_path = path[u] + [v]

                # Shorter path found
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    path[v] = new_path
                    hq.heappush(pq, (new_dist, v))

        if dist[dest] == float("inf"):
            return [-1]

        return path[dest]