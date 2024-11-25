"""
Min Heap Implementation

Description:
A Min Heap is a complete binary tree where the value at each node is less than or equal to the values of its children. It is commonly used to implement priority queues and efficient algorithms like Dijkstra's shortest path.

Logic:
- The heap is represented as a list where the parent-child relationships are determined by index calculations.
- Insertion adds the new element at the end of the list and then "bubbles up" to maintain the heap property.
- Deletion removes the root element (minimum), replaces it with the last element, and then "bubbles down" to maintain the heap property.
- Additional methods include heapify, peek, and size.

Time Complexity:
- Insertion: O(log n)
- Deletion: O(log n)
- Peek: O(1)
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def peek(self):
        """Return the smallest key without removing it."""
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        """Remove and return the smallest key from the heap."""
        if not self.heap:
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._bubble_down(0)
        return min_val

    def _bubble_up(self, index):
        """Move the element at index up to maintain heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Swap
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        """Move the element at index down to maintain heap property."""
        n = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def _heapify(self, arr):
        """Build a heap from an arbitrary array."""
        self.heap = arr[:]
        n = len(self.heap)
        for i in range((n // 2) -1, -1, -1):
            self._bubble_down(i)

def main():
    min_heap = MinHeap()
    elements = [5, 3, 8, 4, 1, 2]
    for elem in elements:
        min_heap.insert(elem)
    print("Min Heap:", min_heap.heap)
    print("Minimum Element:", min_heap.peek())
    print("Extracted Min:", min_heap.extract_min())
    print("Min Heap after extraction:", min_heap.heap)

if __name__ == "__main__":
    main()
