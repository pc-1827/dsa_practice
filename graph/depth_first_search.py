"""
Depth First Search (DFS)

Description:
Depth First Search is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It is used to traverse or search tree or graph data structures.

Logic:
- Start from a selected node.
- Visit the node and mark it as visited.
- Recursively visit all the adjacent unvisited nodes.
- Continue the process until all nodes reachable from the starting node are visited.

Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
- O(V) due to the recursion stack and visited list.
"""

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        self.adj_list.setdefault(u, []).append(v)
        self.adj_list.setdefault(v, []).append(u)  # For undirected graph

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.adj_list.get(v, []):
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

def main():
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    print("DFS Traversal starting from node 'A':")
    graph.dfs('A')  # Output: A B D E C F

if __name__ == "__main__":
    main()
