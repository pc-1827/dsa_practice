"""
Breadth First Search (BFS)

Description:
Breadth First Search is a graph traversal algorithm that explores all neighbors of a node before moving to the next level of nodes. It is used to find the shortest path in unweighted graphs and for level-order traversal.

Logic:
- Start from a selected node.
- Visit the node and enqueue it.
- Dequeue a node from the queue, visit all its unvisited adjacent nodes, and enqueue them.
- Continue the process until the queue is empty.

Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
- O(V) due to the queue and visited list.
"""

from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        self.adj_list.setdefault(u, []).append(v)
        self.adj_list.setdefault(v, []).append(u)  # For undirected graph

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbour in self.adj_list.get(vertex, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

def main():
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    print("BFS Traversal starting from node 'A':")
    graph.bfs('A')  # Output: A B C D E F

if __name__ == "__main__":
    main()
