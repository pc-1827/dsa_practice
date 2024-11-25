"""
Priority Queue Implementation

Description:
A Priority Queue is an abstract data type where each element has a priority. Elements are dequeued based on their priority, not just their insertion order.

Logic:
- Use a heap (max-heap or min-heap) to maintain the order of elements based on priority.
- Enqueue operation adds the element to the heap.
- Dequeue operation removes the element with the highest priority.

Time Complexity:
- Enqueue: O(log n)
- Dequeue: O(log n)

Space Complexity:
- O(n)
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))
        print(f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        if not self.heap:
            print("Priority Queue is empty.")
            return None
        priority, item = heapq.heappop(self.heap)
        print(f"Dequeued: {item} with priority {-priority}")
        return item

    def is_empty(self):
        return len(self.heap) ==0

    def peek(self):
        if not self.heap:
            print("Priority Queue is empty.")
            return None
        return self.heap[0][1]

    def display(self):
        print("Priority Queue:", [(item, -priority) for priority, item in self.heap])

def main():
    pq = PriorityQueue()
    pq.enqueue("task1", 2)
    pq.enqueue("task2", 1)
    pq.enqueue("task3", 3)
    pq.display()
    pq.dequeue()
    pq.display()
    print(f"Top priority task is {pq.peek()}")

if __name__ == "__main__":
    main()
