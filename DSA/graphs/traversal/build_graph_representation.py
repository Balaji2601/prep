from collections import defaultdict


class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    def build_adjacency_list(self):
        adj = defaultdict(list)
        
        for u, v in self.edges:
            # u ---edge---> v
            adj[u].append(v)
        return adj

if __name__ == "__main__":
    n = 4 # no of vertice(V)
    edges = [[1, 0], [2, 0], [2,1], [3,1]]

    practice_graph = Graph(n, edges)
    print(practice_graph.build_adjacency_list())