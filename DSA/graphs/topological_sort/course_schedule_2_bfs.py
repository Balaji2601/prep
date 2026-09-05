# https://leetcode.com/problems/course-schedule-ii/description/

from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, V: int, mp: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_order = [0]*V

        for u, v in mp:
            adj[v].append(u)
            in_order[u] += 1
        
        que = deque([])
        for i in range(V):
            if in_order[i] == 0:
                que.append(i)
        
        ans = []
        count = 0
        while que:
            u = que.popleft()
            ans.append(u)
            count += 1

            for v in adj[u]:
                in_order[v] -= 1

                if in_order[v] == 0:
                    que.append(v)
        
        if count == V:
            return ans
        return []