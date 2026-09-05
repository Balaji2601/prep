# https://leetcode.com/problems/is-graph-bipartite/description/
# https://www.geeksforgeeks.org/problems/bipartite-graph/1

from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def check_bipartite_BFS(graph, currNode, color, currColor):
            que = deque([])
            que.append(currNode)
            color[currNode] = currColor

            while que:
                u = que.popleft()

                for v in graph[u]:
                    if color[v] == color[u]:
                        return False
                    if color[v] == -1:
                        color[v] = 1-color[u]
                        que.append(v)
            return True
                
            

        V = len(graph)
        color = [-1]*V

        for i in range(V):
            if color[i] == -1:
                if check_bipartite_BFS(graph, i, color, 1) == False:
                    return False
        
        return True