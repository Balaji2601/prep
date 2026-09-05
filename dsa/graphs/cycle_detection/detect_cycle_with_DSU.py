# https://www.geeksforgeeks.org/problems/detect-cycle-using-dsu/1

class Solution:
    def detectCycle(self, V, adj):
        def find(i, parent):
            if parent[i] == i:
                return i

            parent[i] = find(parent[i], parent)
            return parent[i]

        def union(x, y, parent, rank):
            parent_of_x = find(x, parent)
            parent_of_y = find(y, parent)

            if parent_of_x == parent_of_y:
                return

            if rank[parent_of_x] > rank[parent_of_y]:
                parent[parent_of_y] = parent_of_x

            elif rank[parent_of_x] < rank[parent_of_y]:
                parent[parent_of_x] = parent_of_y

            else:
                parent[parent_of_x] = parent_of_y
                rank[parent_of_y] += 1

        parent = [i for i in range(V)]
        rank = [0] * V

        for u in range(V):
            for v in adj[u]:
                if u < v:
                    parent_of_u = find(u, parent)
                    parent_of_v = find(v, parent)

                    if parent_of_u == parent_of_v:
                        return True

                    union(u, v, parent, rank)

        return False