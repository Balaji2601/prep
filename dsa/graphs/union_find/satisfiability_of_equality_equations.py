# https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find_parent(i, parent):
            if i == parent[i]:
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
        
        parent = [i for i in range(26)]
        rank = [0]*26

        for s in equations:
            if s[1] == "=":
                union(ord(s[0])-ord("a"), ord(s[-1])-ord("a"), parent, rank)
        
        for s in equations:
            if s[1] == "!":
                first = s[0]
                second = s[-1]

                parent_of_first = find_parent(ord(first)-ord("a"), parent)
                parent_of_second = find_parent(ord(second)-ord("a"), parent)

                if parent_of_first == parent_of_second:
                    return False
        
        return True
