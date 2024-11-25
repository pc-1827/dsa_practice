"""
Floyd-Warshall Algorithm

Description:
The Floyd-Warshall Algorithm computes the shortest paths between all pairs of nodes in a weighted graph. It can handle positive and negative edge weights but not negative cycles.

Logic:
- Initialize a distance matrix where dist[i][j] is the direct edge weight from i to j, or infinity if no direct edge exists.
- Iterate through each node as an intermediate point and update the distance matrix if a shorter path is found through the intermediate node.
- Detect negative cycles if any distance from a node to itself becomes negative.

Time Complexity:
- O(V^3)

Space Complexity:
- O(V^2)
"""

def floyd_warshall(graph, V):
    dist = [[float('infty') for _ in range(V)] for _ in range(V)]
    for u in range(V):
        dist[u][u] = 0
    for u, v, weight in graph['edges']:
        dist[u][v] = weight
    # Update distances
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != float('infty') and dist[k][j] != float('infty'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    # Check for negative cycles
    for i in range(V):
        if dist[i][i] < 0:
            print("Graph contains a negative-weight cycle.")
            return None
    return dist

def main():
    graph = {
        'vertices': 4,
        'edges': [
            (0, 1, 5),
            (0, 3, 10),
            (1, 2, 3),
            (2, 3, 1),
            (3, 1, -2)
        ]
    }
    V = graph['vertices']
    distances = floyd_warshall(graph, V)
    if distances:
        print("Shortest distances between all pairs of vertices:")
        for i in range(V):
            for j in range(V):
                if distances[i][j] == float('infty'):
                    print(f"Distance from {i} to {j}: INF")
                else:
                    print(f"Distance from {i} to {j}: {distances[i][j]}")
            print()

if __name__ == "__main__":
        main()
