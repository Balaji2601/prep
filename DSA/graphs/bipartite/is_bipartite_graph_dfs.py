# https://www.geeksforgeeks.org/problems/bipartite-graph/1
# https://leetcode.com/problems/is-graph-bipartite/description/

from collections import defaultdict


class Solution:
    def isBipartite(self, V, edges):

        def check_bipartite_DFS(adj, u, color, currColor):
            color[u] = currColor

            for v in adj[u]:
                if color[v] == color[u]: # If color of adj v node is same as u node then it is not a bipartite graph
                    return False
                if color[v] == -1: # If color[v] == -1 meaning v is not visited then we have to dfs on that
                    color_of_v = 1 - color[u] # Giving the neighbour v the opposite colour of the current node u.
                    if check_bipartite_DFS(adj, v, color, color_of_v) == False:
                        return False

            return True

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # -1 in color indicates the node i is not visited and not coloured
        color = [-1]*V

        # red = 1
        # grenn = 0

        for i in range(V):
            if color[i] == -1:
                if check_bipartite_DFS(adj, i, color, 1) == False: # start the first node of a graph with red color(it is a choice)
                    return False

        return True
