"""
Simple Queue Implementation

Description:
A Simple Queue follows the First-In-First-Out (FIFO) principle. Elements are added to the rear and removed from the front.

Logic:
- Use a list to store elements.
- Enqueue operation appends to the list.
- Dequeue operation removes from the front using pop(0).

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(n) due to list reordering

Space Complexity:
- O(n)
"""

class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item

    def is_empty(self):
        return len(self.queue) ==0

    def peek(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue[0]

    def display(self):
        print("Queue:", self.queue)

def main():
    q = SimpleQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()
    print(f"Front element is {q.peek()}")

if __name__ == "__main__":
    main()
