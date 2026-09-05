# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

from collections import defaultdict
import heapq
from typing import List

# prims
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def prims_algo(adj, V):
            pq = [(0,0)] # wt, v
            ans = 0
            inMST = [False]*V

            while pq:
                wt, u = heapq.heappop(pq)

                if inMST[u]: # if visited
                    continue
                
                inMST[u] = True
                ans += wt

                for v, n_wt in adj[u]:
                    if not inMST[v]:
                        heapq.heappush(pq, (n_wt, v))
            
            return ans

        adj = defaultdict(list)
        V = len(points)
        for i in range(V):
            for j in range(i+1, V):
                x1 = points[i][0]
                y1 = points[i][1]

                x2 = points[j][0]
                y2 = points[j][1]
                
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((j,dist))
                adj[j].append((i,dist))
        
        return prims_algo(adj, V)

# kruskals
class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)
        parent = [i for i in range(V)]
        rank = [0]*V

        def find_parent(i):
            if parent[i] == i:
                return i
            parent[i] = find_parent(parent[i])
            return parent[i]
        
        def union(x,y):
            parent_of_x = find_parent(x)
            parent_of_y = find_parent(y)

            if parent_of_x == parent_of_y:
                return
            
            if rank[parent_of_x] > rank[parent_of_y]:
                parent[parent_of_y] = parent_of_x
            
            elif rank[parent_of_x] < rank[parent_of_y]:
                parent[parent_of_x] = parent_of_y
            
            else:
                parent[parent_of_x] = parent_of_y
                rank[parent_of_y] += 1
        
        def kruskal(edges):
            ans = 0
            for u,v,wt in edges:
                parent_of_u = find_parent(u)
                parent_of_v = find_parent(v)

                if parent_of_u != parent_of_v:
                    union(u,v)
                    ans += wt
            return ans

        edges = []
        for i in range(V):
            for j in range(i+1, V):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([i,j,dist])
                # edges.append([j,i,dist])
        
        edges.sort(key = lambda x: x[2])

        return kruskal(edges)
            

