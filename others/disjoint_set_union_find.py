"""
Disjoint Set (Union-Find) Implementation

Description:
The Disjoint Set data structure, also known as Union-Find, keeps track of a set of elements partitioned into disjoint (non-overlapping) subsets. It provides near-constant-time operations to add new sets, merge existing sets, and find the representative of a set.

Logic:
- Each element points to a parent, forming trees. Initially, each element is its own parent.
- **Find**: Determines the root of the set containing the element, with path compression for optimization.
- **Union**: Merges two sets by attaching the root of one to the root of the other, using union by rank to maintain a balanced tree structure.

Time Complexity:
- Amortized O(α(n)) per operation, where α is the inverse Ackermann function, practically constant.
"""

class DisjointSet:
    def __init__(self, n):
        """Initialize n disjoint sets."""
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find the representative of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y using union by rank."""
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return  # Already in the same set

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] +=1

def main():
    # Example usage
    ds = DisjointSet(5)
    ds.union(0, 2)
    ds.union(4, 2)
    ds.union(3, 1)
    print("Sets after unions:")
    for i in range(5):
        print(f"Element {i} is in set {ds.find(i)}")

    ds.union(3, 4)
    print("\nSets after union(3, 4):")
    for i in range(5):
        print(f"Element {i} is in set {ds.find(i)}")

if __name__ == "__main__":
    main()
