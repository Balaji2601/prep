# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, V: int, mp: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_order = [0]*V
        for u, v in mp:
            adj[v].append(u)
            in_order[u] += 1
        
        que = deque([])
        for i in range(V):
            if in_order[i] == 0:
                que.append(i)
        
        while que:
            u = que.popleft()

            for v in adj[u]:
                in_order[v] -= 1

                if in_order[v] == 0:
                    que.append(v)
        
        count = 0
        for i in range(V):
            if in_order[i] == 0:
                count += 1
            
        return count == V

