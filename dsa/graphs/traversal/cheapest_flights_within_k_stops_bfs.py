# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# https://www.youtube.com/watch?v=VmUpydhNmuw&t=915s

from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))

        distance = [float("inf")] * n
        distance[src] = 0

        queue = deque([(src, 0)])  # (node, cost)
        level = 0

        while queue and level <= k:
            for _ in range(len(queue)):
                u, d = queue.popleft()
                for v, cost in adj[u]:
                    if d + cost < distance[v]:
                        distance[v] = d + cost
                        queue.append((v, d + cost))
            level += 1

        return -1 if distance[dst] == float("inf") else distance[dst]
