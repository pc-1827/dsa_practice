"""
Max Heap Implementation

Description:
A Max Heap is a complete binary tree where the value at each node is greater than or equal to the values of its children. It is commonly used to implement priority queues and efficient algorithms like Heap Sort.

Logic:
- The heap is represented as a list where the parent-child relationships are determined by index calculations.
- Insertion adds the new element at the end of the list and then "bubbles up" to maintain the heap property.
- Deletion removes the root element (maximum), replaces it with the last element, and then "bubbles down" to maintain the heap property.
- Additional methods include heapify, peek, and size.

Time Complexity:
- Insertion: O(log n)
- Deletion: O(log n)
- Peek: O(1)
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def peek(self):
        """Return the largest key without removing it."""
        if not self.heap:
            return None
        return self.heap[0]

    def extract_max(self):
        """Remove and return the largest key from the heap."""
        if not self.heap:
            return None
        max_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._bubble_down(0)
        return max_val

    def _bubble_up(self, index):
        """Move the element at index up to maintain heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            # Swap
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        """Move the element at index down to maintain heap property."""
        n = len(self.heap)
        while True:
            largest = index
            left = 2 * index +1
            right = 2 * index +2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
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
    max_heap = MaxHeap()
    elements = [3, 1, 6, 5, 2, 4]
    for elem in elements:
        max_heap.insert(elem)
    print("Max Heap:", max_heap.heap)
    print("Maximum Element:", max_heap.peek())
    print("Extracted Max:", max_heap.extract_max())
    print("Max Heap after extraction:", max_heap.heap)

if __name__ == "__main__":
    main()
