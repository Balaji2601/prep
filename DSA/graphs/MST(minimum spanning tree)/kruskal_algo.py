# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
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

                # if parents of u,v are different then both belong to different components
                # we need to combine them into single component.
                if parent_of_u != parent_of_v:
                    union(u,v)
                    ans+=wt
            return ans
        
        # Sort the edges with weights then apply kruskal so minimum weight edge will  
        # be connected first acc to kruskal algorithm
        edges.sort(key = lambda x: x[2])
        
        return kruskal(edges)