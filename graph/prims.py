"""
Prim's Algorithm

Description:
Prim's Algorithm is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges. It grows the MST by adding the cheapest possible connection from the tree to another vertex.

Logic:
- Initialize a tree with a single vertex, chosen arbitrarily.
- At each step, add the shortest edge that connects a vertex in the tree to a vertex outside the tree.
- Repeat until all vertices are included in the tree.

Time Complexity:
- O(E log V) using a priority queue.

Space Complexity:
- O(V + E)
"""

import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def prim_mst(self):
        key = [float('infty')] * self.V
        parent = [None] * self.V
        key[0] = 0
        min_heap = [(0, 0)]
        in_mst = [False] * self.V

        while min_heap:
            current_key, u = heapq.heappop(min_heap)
            if in_mst[u]:
                continue
            in_mst[u] = True

            for v, weight in self.adj_list[u]:
                if not in_mst[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
                    heapq.heappush(min_heap, (key[v], v))

        # Print MST
        print("Edge \tWeight")
        for v in range(1, self.V):
            print(f"{parent[v]} - {v} \t{key[v]}")

def main():
    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    print("Minimum Spanning Tree using Prim's Algorithm:")
    graph.prim_mst()

if __name__ == "__main__":
        main()
