"""
Dijkstra's Algorithm

Description:
Dijkstra's Algorithm is used to find the shortest path from a single source node to all other nodes in a weighted graph with non-negative edge weights.

Logic:
- Initialize distances from the source to all nodes as infinity, except the source itself which is zero.
- Use a priority queue to select the node with the smallest distance.
- Update the distances of adjacent nodes if a shorter path is found through the current node.
- Repeat the process until all nodes are processed.

Time Complexity:
- O((V + E) log V) using a priority queue.

Space Complexity:
- O(V + E)
"""

import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        self.adj_list.setdefault(u, []).append((v, weight))
        self.adj_list.setdefault(v, []).append((u, weight))  # For undirected graph

    def dijkstra(self, start):
        distances = {vertex: float('infty') for vertex in self.adj_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.adj_list.get(current_vertex, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

def main():
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'Z', 6)
    graph.add_edge('E', 'Z', 3)
    start_node = 'A'
    distances = graph.dijkstra(start_node)
    print(f"Shortest distances from node {start_node}:")
    for vertex in distances:
        print(f"Distance to {vertex}: {distances[vertex]}")

if __name__ == "__main__":
        main()
