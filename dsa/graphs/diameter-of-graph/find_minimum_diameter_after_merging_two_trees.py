# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
# solution link - https://www.youtube.com/watch?v=uz_WISpySFs&list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY&index=45

from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def diameter(adj, src, V):
            q = deque([src])
            farthest_node = src
            visited = [False]*V
            visited[src] = True
            level = 0
            while q:
                size = len(q)
                for _ in range(size):
                    u = q.popleft()
                    farthest_node = u
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                # if queue is non empty only we will move to next level
                if q:
                    level += 1
                
            return farthest_node, level
        
        def find_diameter(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            V = len(edges)+1
            src = 0
            # Farthest node(A) from random node src here we took 0 as random node
            # this step gives one end of diameter ie A
            farthest_node_from_src, _ = diameter(adj, src, V)

            # Farthest node(B) from farthest_node(A)
            # this step will give other end of diameter ie B
            _, level = diameter(adj, farthest_node_from_src, V)

            return level


        d1 = find_diameter(edges1)
        d2 = find_diameter(edges2)
        # (di+1)//2 gives mid of edgesi and adding 1 at the end because
        # while combining two trees we need a edge right
        combined_diameter = (d1+1)//2 + (d2+1)//2 + 1 
        # we do the max(combined, d1, d2) because if combined < (d1 or d2)
        # then combined diameter should be either d1 or d2.
        # see video link attached if needed more clarification.
        ans = max(combined_diameter, d1, d2)
        return ans