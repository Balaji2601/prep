# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

from collections import defaultdict
import heapq

class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))

        # in the given question they only asked about the sum of MST
        # if they asked path we need to store the (wt, node(ie v), parent_of_node_v(ie u)) 
        # (0,0,-1) wt == 0 because -1 --> 0 there is no weight right?
        # parent_array is parent = [-1]*V initially all the nodes parent is -1(unknown)
        pq = [(0,0)] # (wt, node)
        inMST = [False]*V
        ans = 0 # sum of all edges in a MST of the given adj graph

        # O(ElogE)
        # O(E)
        while pq:
            wt, u = heapq.heappop(pq) # O(logE)
            
            # if u is visited then continue
            if inMST[u] == True:
                continue

            inMST[u] = True # marking the u as visited
            ans += wt
            
            for v,n_wt in adj[u]: # n_wt = neighbour weight
                if not inMST[v]:
                    heapq.heappush(pq, (n_wt,v)) # O(logE)
        
        return ans
                