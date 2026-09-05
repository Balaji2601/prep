# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq as hq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, wt in times:
            adj[u].append((v, wt))
        
        result = [float("inf")]*(n+1)
        result[k] = 0
        pq = [(0, k)]

        while pq:
            d, u = hq.heappop(pq)

            if d > result[u]:
                continue
            
            for v, wt in adj[u]:
                if d+wt < result[v]:
                    result[v] = d+wt
                    hq.heappush(pq, (result[v], v))
        
        for i in range(1, n+1):
            if result[i] == float("inf"):
                return -1
        

        return max(result[1:])

        