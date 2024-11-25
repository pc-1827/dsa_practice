"""
Segment Tree

Description:
A Segment Tree is a binary tree used for storing information about intervals or segments. It allows querying which of the stored segments contain a given point efficiently and can be used for various range query problems like range sum, range minimum, etc.

Logic:
- The tree is built by recursively dividing the array into halves.
- Each node represents a segment and stores aggregated information (e.g., sum, min).
- Queries and updates are performed by traversing the tree from root to leaves.

Time Complexity:
- Building the tree: O(n)
- Query: O(log n)
- Update: O(log n)
"""

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<=1
        self.tree = [0]*(2*self.size)
        self.build(data)

    def build(self, data):
        # Insert leaf nodes in the tree
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # Build the segment tree by calculating parents
        for i in range(self.size -1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i +1]

    def update(self, index, value):
        # Set value at position index
        index += self.size
        self.tree[index] = value
        while index >1:
            index >>=1
            self.tree[index] = self.tree[2*index] + self.tree[2*index +1]

    def query(self, l, r):
        # Sum on interval [l, r)
        res = 0
        l += self.size
        r += self.size
        while l < r:
            if l &1:
                res += self.tree[l]
                l +=1
            if r &1:
                r -=1
                res += self.tree[r]
            l >>=1
            r >>=1
        return res

def main():
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(data)
    print("Initial Segment Tree:")
    print(seg_tree.tree)

    print("\nSum of values in range [1, 5):", seg_tree.query(1,5))  # Output: 3+5+7+9 =24

    seg_tree.update(3, 10)
    print("\nSegment Tree after updating index 3 to 10:")
    print(seg_tree.tree)

    print("\nSum of values in range [1, 5):", seg_tree.query(1,5))  # Output: 3+5+10+9 =27

if __name__ == "__main__":
    main()
