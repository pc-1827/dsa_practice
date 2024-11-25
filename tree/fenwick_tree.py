"""
Fenwick Tree (Binary Indexed Tree)

Description:
A Fenwick Tree, or Binary Indexed Tree (BIT), is a data structure that provides efficient methods for cumulative frequency tables. It allows querying prefix sums and updating elements in logarithmic time.

Logic:
- The tree is represented as an array where each element stores the sum of a range of elements.
- To update an element, propagate the change to all relevant nodes.
- To query the prefix sum, aggregate the sums from relevant nodes.

Time Complexity:
- Update: O(log n)
- Query: O(log n)
"""

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0]*(self.size +1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        result =0
        while index >0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

def main():
    data = [3, 2, -1, 6, 5, 4, -3]
    size = len(data)
    ft = FenwickTree(size)
    for i in range(1, size +1):
        ft.update(i, data[i-1])

    print("Initial Fenwick Tree:")
    print(ft.tree)

    print("\nPrefix sum up to index 5:", ft.query(5))  # Output: 3+2+(-1)+6+5 =15
    print("Range sum [2, 5]:", ft.range_query(2,5))   # Output:2+(-1)+6+5=12

    ft.update(3, 3)  # Update index 3 by adding 3, data[2] becomes 2
    print("\nFenwick Tree after updating index 3 by 3:")
    print(ft.tree)

    print("\nPrefix sum up to index 5:", ft.query(5))  # Output:3+2+2+6+5=18
    print("Range sum [2, 5]:", ft.range_query(2,5))   # Output:2+2+6+5=15

if __name__ == "__main__":
    main()
