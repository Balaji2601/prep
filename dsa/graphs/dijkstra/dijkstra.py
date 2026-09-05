# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

from collections import defaultdict
import heapq as hq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        result = [float("inf")]*V # initializing distances from src to all vertices as inf(MAX_INT)
        
        result[src] = 0 # from src ---> src the shortest distance is zero right
        pq = []
        hq.heappush(pq, (0, src)) # pushing it to the min_heap
        
        while pq:
            dist, node = hq.heappop(pq)
             # check if the current node distance dist from the node is greater than in the result
             # if it is greater than what in the result then we already found the distance to the node 
             # from source, then going further does not make sense with dist. 
             # So continue.
            if dist > result[node]:
                continue
            for v,wt in adj[node]:
                if dist+wt < result[v]:
                    result[v] = dist+wt
                    hq.heappush(pq, (dist+wt,v))
        
        return result