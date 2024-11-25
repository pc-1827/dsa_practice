"""
Kruskal's Algorithm

Description:
Kruskal's Algorithm is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges. It builds the MST by adding edges in increasing order of weight, ensuring no cycles are formed.

Logic:
- Sort all the edges in non-decreasing order of their weight.
- Initialize a Union-Find structure to detect cycles.
- Iterate through the sorted edges and add them to the MST if they don't form a cycle.
- Continue until the MST contains V-1 edges.

Time Complexity:
- O(E log E) due to sorting, where E is the number of edges.

Space Complexity:
- O(V + E)
"""

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0]*size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False  # Already in the same set
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[u_root] +=1
        return True

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def kruskal_mst(self):
        self.edges.sort()
        uf = UnionFind(self.V)
        mst = []
        for weight, u, v in self.edges:
            if uf.union(u, v):
                mst.append((u, v, weight))
            if len(mst) == self.V -1:
                break
        # Print MST
        print("Edge \tWeight")
        for u, v, weight in mst:
            print(f"{u} - {v} \t{weight}")

def main():
    graph = Graph(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)

    print("Minimum Spanning Tree using Kruskal's Algorithm:")
    graph.kruskal_mst()

if __name__ == "__main__":
        main()
