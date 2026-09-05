# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        result = [float("inf")] * n
        result[src] = 0

        # relax edges k+1 times (k stops = k+1 edges)
        for i in range(k + 1):
            # temp = result[:] prevents using updated values within the same iteration
            temp = result[:]
            for u, v, cost in flights:
                if result[u] != float("inf") and result[u] + cost < temp[v]:
                    temp[v] = result[u] + cost
            result = temp

        return -1 if result[dst] == float("inf") else result[dst]
