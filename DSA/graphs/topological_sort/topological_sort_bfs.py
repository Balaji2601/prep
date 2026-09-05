# Kahn's algorithm
# https://www.geeksforgeeks.org/problems/topological-sort/1

from collections import defaultdict, deque

class Solution:
    def topo_sort(self, V, edges):
        adj = defaultdict(list)
        in_degree = [0]*V

        # 1. Populate in_degree counts
        for u,v in edges:
            adj[u].append(v)
            in_degree[v] += 1

        # 2. Add in_degree count = 0 nodes into the que

        que = deque([])

        for i in range(V):
            if in_degree[i] == 0:
                que.append(i)

        # 3. Do BFS on the que

        result = []
        while que:
            u = que.popleft()
            result.append(u)

            for v in adj[u]:
                in_degree[v] -= 1

                if in_degree[v] == 0:
                    que.append(v)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.topo_sort(V = 4, edges= [[3, 0], [1, 0], [2, 0]]))

        