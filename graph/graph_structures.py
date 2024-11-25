"""
Graph Structures: Adjacency Matrix, Adjacency List, and Edge List

Description:
This module implements graph data structures using three different representations:
1. Adjacency Matrix
2. Adjacency List
3. Edge List

It also provides methods to add and remove nodes and edges from the graph.

Logic:
- **Adjacency Matrix**: Represents the graph as a 2D matrix where the cell at [i][j] indicates the presence (and weight) of an edge between node i and node j.
- **Adjacency List**: Represents the graph as a list of lists, where each list corresponds to a node and contains its adjacent nodes and edge weights.
- **Edge List**: Represents the graph as a list of tuples, each containing a pair of nodes and the weight of the edge between them.

Methods:
- `add_node(node)`: Adds a node to the graph.
- `remove_node(node)`: Removes a node and all associated edges from the graph.
- `add_edge(node1, node2, weight=1)`: Adds an edge between two nodes with an optional weight.
- `remove_edge(node1, node2)`: Removes the edge between two nodes.
"""

class Graph:
    def __init__(self, representation='adjacency_list'):
        if representation not in ['adjacency_matrix', 'adjacency_list', 'edge_list']:
            raise ValueError("Unsupported graph representation.")
        self.representation = representation
        self.nodes = set()
        if self.representation == 'adjacency_matrix':
            self.matrix = []
            self.node_indices = {}
        elif self.representation == 'adjacency_list':
            self.adj_list = {}
        elif self.representation == 'edge_list':
            self.edge_list = []

    def add_node(self, node):
        if node in self.nodes:
            print(f"Node {node} already exists.")
            return
        self.nodes.add(node)
        if self.representation == 'adjacency_matrix':
            self.node_indices[node] = len(self.node_indices)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * (len(self.node_indices)))
        elif self.representation == 'adjacency_list':
            self.adj_list[node] = []
        elif self.representation == 'edge_list':
            pass  # No action needed for edge list

    def remove_node(self, node):
        if node not in self.nodes:
            print(f"Node {node} does not exist.")
            return
        self.nodes.remove(node)
        if self.representation == 'adjacency_matrix':
            index = self.node_indices.pop(node)
            self.matrix.pop(index)
            for row in self.matrix:
                row.pop(index)
            # Update indices
            self.node_indices = {n: i for i, n in enumerate(self.node_indices)}
        elif self.representation == 'adjacency_list':
            self.adj_list.pop(node)
            for adj in self.adj_list.values():
                adj[:] = [edge for edge in adj if edge[0] != node]
        elif self.representation == 'edge_list':
            self.edge_list = [edge for edge in self.edge_list if edge[0] != node and edge[1] != node]

    def add_edge(self, node1, node2, weight=1):
        if node1 not in self.nodes or node2 not in self.nodes:
            print("Both nodes must exist in the graph.")
            return
        if self.representation == 'adjacency_matrix':
            index1 = self.node_indices[node1]
            index2 = self.node_indices[node2]
            self.matrix[index1][index2] = weight
            self.matrix[index2][index1] = weight  # For undirected graph
        elif self.representation == 'adjacency_list':
            self.adj_list[node1].append((node2, weight))
            self.adj_list[node2].append((node1, weight))  # For undirected graph
        elif self.representation == 'edge_list':
            self.edge_list.append((node1, node2, weight))

    def remove_edge(self, node1, node2):
        if self.representation == 'adjacency_matrix':
            if node1 in self.node_indices and node2 in self.node_indices:
                index1 = self.node_indices[node1]
                index2 = self.node_indices[node2]
                self.matrix[index1][index2] = 0
                self.matrix[index2][index1] = 0
        elif self.representation == 'adjacency_list':
            if node1 in self.adj_list:
                self.adj_list[node1] = [edge for edge in self.adj_list[node1] if edge[0] != node2]
            if node2 in self.adj_list:
                self.adj_list[node2] = [edge for edge in self.adj_list[node2] if edge[0] != node1]
        elif self.representation == 'edge_list':
            self.edge_list = [edge for edge in self.edge_list if not ((edge[0] == node1 and edge[1] == node2) or (edge[0] == node2 and edge[1] == node1))]

def main():
    # Example usage with Adjacency List
    graph = Graph(representation='adjacency_list')
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_edge('A', 'B', 5)
    graph.add_edge('B', 'C', 3)
    graph.add_edge('A', 'C', 4)
    print("Adjacency List:", graph.adj_list)

    # Example usage with Adjacency Matrix
    graph_matrix = Graph(representation='adjacency_matrix')
    graph_matrix.add_node('A')
    graph_matrix.add_node('B')
    graph_matrix.add_node('C')
    graph_matrix.add_edge('A', 'B', 5)
    graph_matrix.add_edge('B', 'C', 3)
    graph_matrix.add_edge('A', 'C', 4)
    print("Adjacency Matrix:", graph_matrix.matrix)

    # Example usage with Edge List
    graph_edge = Graph(representation='edge_list')
    graph_edge.add_node('A')
    graph_edge.add_node('B')
    graph_edge.add_node('C')
    graph_edge.add_edge('A', 'B', 5)
    graph_edge.add_edge('B', 'C', 3)
    graph_edge.add_edge('A', 'C', 4)
    print("Edge List:", graph_edge.edge_list)

if __name__ == "__main__":
    main()
