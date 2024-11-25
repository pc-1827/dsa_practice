"""
Kosaraju's Algorithm (Strongly Connected Components)

Description:
Kosaraju's Algorithm identifies all strongly connected components (SCCs) in a directed graph. It works by performing two Depth First Searches (DFS): one on the original graph and one on the transposed graph.

Logic:
- Perform a DFS on the original graph and push nodes onto a stack in the order of completion.
- Transpose the graph (reverse all edges).
- Pop nodes from the stack and perform DFS on the transposed graph to identify SCCs.

Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
- O(V + E)
"""

def kosaraju_scc(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for neighbour in graph.get(v, []):
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(v)

    # Step 1: Fill stack with vertices in the order of completion
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    # Step 2: Transpose the graph
    transposed = {}
    for u in graph:
        for v in graph[u]:
            transposed.setdefault(v, []).append(u)

    # Step 3: Perform DFS on transposed graph
    visited.clear()
    sccs = []

    def dfs_transposed(v, component):
        visited.add(v)
        component.append(v)
        for neighbour in transposed.get(v, []):
            if neighbour not in visited:
                dfs_transposed(neighbour, component)

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = []
            dfs_transposed(vertex, component)
            sccs.append(component)

    return sccs

def main():
    graph = {
        'A': ['B'],
        'B': ['C', 'E', 'F'],
        'C': ['D', 'G'],
        'D': ['C', 'H'],
        'E': ['A', 'F'],
        'F': ['G'],
        'G': ['F'],
        'H': ['D', 'G']
    }
    sccs = kosaraju_scc(graph)
    print("Strongly Connected Components:")
    for scc in sccs:
        print(scc)

if __name__ == "__main__":
        main()
