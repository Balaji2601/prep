# https://leetcode.com/problems/count-the-number-of-complete-components/description/

#DSU
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        # Step 1: Write union find
        def find_parent(i, parent):
            if parent[i] == i:
                return i
            parent[i] = find_parent(parent[i], parent)
            return parent[i]
        
        def union(x, y, parent, rank):
            parent_of_x = find_parent(x, parent)
            parent_of_y = find_parent(y, parent)

            if parent_of_x == parent_of_y:
                return
            
            if rank[parent_of_x] > rank[parent_of_y]:
                parent[parent_of_y] = parent_of_x
            
            elif rank[parent_of_x] < rank[parent_of_y]:
                parent[parent_of_x] = parent_of_y

            else:
                parent[parent_of_x] = parent_of_y
                rank[parent_of_y] += 1

        parent = [i for i in range(n)]
        rank = [0]*n

        # Step 2: Find components
        for u, size in edges:
            parent_of_u = find_parent(u, parent)
            parent_of_v = find_parent(size, parent)

            if parent_of_u == parent_of_v:
                continue
            
            union(u, size, parent, rank)
        

        # Step 3: Populate mp with parent(component) -> size of component
        mp = defaultdict(int)
        # To find size of each component, we calculate parent of each node. 
        # We get unique parents count. As each component represents different parents. 
        # You will get a doubt saying what does parent array doing. 
        # Why we need to calculate again. 
        # Because sometimes some nodes will have sub-parents, if we calculate again we get path-compressed parent. 
        # And all nodes in a component have same parent. And each component have different parent.
        # mp contains parent(component) -> size of the component.
        for i in range(n):
            parent_of_i = find_parent(i, parent)
            mp[parent_of_i] += 1
        

        
        # Step 4: Find result
        # formula is size*(remaining-size)
        remaining = n
        result = 0
        for k, size in mp.items():
            result += size*(remaining - size)
            remaining -= size
        
        return result

