"""
Tarjan's Algorithm (Strongly Connected Components)

Description:
Tarjan's Algorithm identifies all strongly connected components (SCCs) in a directed graph. A strongly connected component is a subgraph where every vertex is reachable from every other vertex within the same subgraph.

Logic:
- Perform a Depth First Search (DFS) traversal of the graph.
- Assign each node an index and a low link value.
- Use a stack to keep track of the traversal path.
- When a node's low link value equals its index, it is the root of an SCC.

Time Complexity:
- O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
- O(V)
"""

def tarjans_scc(graph):
    index = 0
    indices = {}
    low_link = {}
    stack = []
    on_stack = set()
    sccs = []

    def strong_connect(v):
        nonlocal index
        indices[v] = index
        low_link[v] = index
        index +=1
        stack.append(v)
        on_stack.add(v)
        for w in graph.get(v, []):
            if w not in indices:
                strong_connect(w)
                low_link[v] = min(low_link[v], low_link[w])
            elif w in on_stack:
                low_link[v] = min(low_link[v], indices[w])
        if low_link[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for vertex in graph:
        if vertex not in indices:
            strong_connect(vertex)
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
    sccs = tarjans_scc(graph)
    print("Strongly Connected Components:")
    for scc in sccs:
        print(scc)

if __name__ == "__main__":
        main()
