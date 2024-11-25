"""
Bellman-Ford Algorithm

Description:
The Bellman-Ford Algorithm computes the shortest paths from a single source node to all other nodes in a weighted graph. It can handle graphs with negative edge weights and detect negative cycles.

Logic:
- Initialize distances from the source to all nodes as infinity, except the source itself which is zero.
- Relax all edges |V| - 1 times, where V is the number of vertices.
- Check for negative-weight cycles by verifying if any distance can still be reduced.

Time Complexity:
- O(V * E)

Space Complexity:
- O(V)
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, start):
        distances = {v: float('infty') for v in range(self.V)}
        distances[start] = 0
        # Relax edges |V| -1 times
        for _ in range(self.V -1):
            for u, v, weight in self.edges:
                if distances[u] != float('infty') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if distances[u] != float('infty') and distances[u] + weight < distances[v]:
                print("Graph contains a negative-weight cycle.")
                return None
        return distances

def main():
    graph = Graph(5)
    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)
    graph.add_edge(3, 2, 5)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 3, -3)
    start_vertex = 0
    distances = graph.bellman_ford(start_vertex)
    if distances:
        print(f"Shortest distances from vertex {start_vertex}:")
        for vertex in distances:
            print(f"Distance to vertex {vertex}: {distances[vertex]}")

if __name__ == "__main__":
        main()
