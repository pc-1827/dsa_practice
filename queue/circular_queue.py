"""
Circular Queue Implementation

Description:
A Circular Queue is a linear data structure that follows the FIFO principle but connects the end back to the front, making it circular. It efficiently utilizes space by reusing empty slots created by dequeued elements.

Logic:
- Initialize a fixed-size list with `front` and `rear` pointers.
- Enqueue operation adds an element at the `rear` and moves the rear pointer.
- Dequeue operation removes an element from the `front` and moves the front pointer.
- The queue is full when the next position of `rear` is `front`.
- The queue is empty when `front` is `-1`.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)

Space Complexity:
- O(n)
"""

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear +1) % self.size == self.front:
            print("Queue is full.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear +1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front +1) % self.size
        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        print("Queue:", end=" ")
        if self.rear >= self.front:
            print(*self.queue[self.front:self.rear+1])
        else:
            print(*self.queue[self.front:self.size], *self.queue[0:self.rear+1])

    def is_empty(self):
        return self.front == -1

def main():
    cq = CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.display()
    cq.enqueue(50)  # Should indicate queue is full
    cq.dequeue()
    cq.enqueue(50)
    cq.display()
    while not cq.is_empty():
        cq.dequeue()
    cq.display()

if __name__ == "__main__":
    main()
