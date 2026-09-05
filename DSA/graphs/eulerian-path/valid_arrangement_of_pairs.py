# https://leetcode.com/problems/valid-arrangement-of-pairs/description/

# print

from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for u,v in pairs:
            adj[u].append(v)
            in_degree[v] += 1
            out_degree[u] += 1

        # if we do not get start_node after looping meaning 
        # it is a euler_circuit and we can start wherever we want, so if we start with pair[0][0] 
        # and if it is not changed after looping then 
        start_node = pairs[0][0]
        for i in adj:
            if out_degree[i]-in_degree[i] == 1:
                start_node = i

        
        stack = [start_node]
        path = []
        while stack:
            u = stack[-1]
            if adj[u]:
                v = adj[u].pop()
                stack.append(v)
            else:
                path.append(u)
                stack.pop()

        path = path[::-1]
        j = 0
        ans = []
        for i in range(1,len(path)):
            ans.append([path[j],path[i]])
            j += 1

        return ans
