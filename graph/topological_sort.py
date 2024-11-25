"""
Topological Sort

Description:
Topological Sort is an ordering of the vertices in a directed acyclic graph (DAG) such that for every directed edge U -> V, vertex U comes before V in the ordering. It is used in scheduling tasks, resolving symbol dependencies, and more.

Logic:
- Use Depth First Search (DFS) to traverse the graph.
- After visiting all descendants of a node, add it to the stack.
- Reverse the stack to get the topological ordering.

Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
- O(V + E)
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.topological_sort_util(neighbour, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = {i: False for i in range(self.V)}
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        return stack

def main():
    graph = Graph(6)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    print("Topological Sort of the given graph:")
    order = graph.topological_sort()
    print(order)  # Output might be [5, 4, 2, 3, 1, 0]

if __name__ == "__main__":
        main()
