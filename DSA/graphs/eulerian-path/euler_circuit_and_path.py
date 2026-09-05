# https://www.geeksforgeeks.org/problems/euler-circuit-and-path/1

class Solution:
    def isEulerCircuit(self, V, adj):
        def DFS(adj, u, visited):
            visited[u] = True

            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, v, visited)

        def isConnected(V, adj):
            first_non_zero_degree_vertex = -1
            for i in range(V):
                if len(adj[i]) != 0:
                    first_non_zero_degree_vertex = i

            visited = [False] * V
            DFS(adj, first_non_zero_degree_vertex, visited)

            # If we get non-visited vertex which have degree > 0 then the vertex is not in a connected component.
            # Which is contradiction to both euler path and circuit
            for i in range(V):
                if visited[i] == False and len(adj[i]) > 0:
                    return False
            return True

        # 1. Check the graph is connected or not for non-zero degree vertices
        if isConnected(V, adj) == False:
            return 0

        odd_degree_vertex_count = 0
        for i in range(V):
            if len(adj[i]) % 2 != 0:
                odd_degree_vertex_count += 1

        # 2. If count of odd degree vertices > 2 then it is not a euler path and circuit
        if odd_degree_vertex_count > 2:
            return 0

        # 3. If count of odd degree vertices == 2 then it is a euler path.
        if odd_degree_vertex_count == 2:
            return 1

        # 4. If count of odd degree vertices == 0 then it is a euler circuit.
        return 2