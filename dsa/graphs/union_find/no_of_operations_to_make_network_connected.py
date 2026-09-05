# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        def find(i, parent):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i], parent)
            return parent[i]

        def union(x, y, parent, rank):
            parent_of_x = find(x,parent)
            parent_of_y = find(y,parent)
            
            if parent_of_x == parent_of_y:
                return
            
            if rank[parent_of_x] > rank[parent_of_y]:
                parent[parent_of_y] = parent_of_x
            
            elif rank[parent_of_x] < rank[parent_of_y]:
                parent[parent_of_x] = parent_of_y
            
            else:
                parent[parent_of_x] = parent_of_y
                rank[parent_of_y] += 1
    

        no_of_connections = len(connections)
        if no_of_connections+1 < n:
            return -1
        
        # first no of components will be because each individual vertex will be a component right
        no_of_components = n

        parent = [i for i in range(n)]
        rank = [0]*n

        for u, v in connections:
            parent_of_u = find(u, parent)
            parent_of_v = find(v, parent)

            if parent_of_u == parent_of_v:
                continue
            
            union(parent_of_u, parent_of_v, parent, rank)
            # after every union we perform the components will become one less as two components will be one after union 
            no_of_components -= 1
        
        # no there will be 1 connected component C1 formed by connections[array] lets say individual left components are C2 
        # and C3. So to connected C1, C2, C3 we need 2 edges which is (3-1). 
        # So if there are Cn components left we need (n-1) edges to connect them into 1 component. 
        # That is the reason no_of_components-1 is the answer.
        return no_of_components - 1