"""
Deque (Double-ended Queue) Implementation

Description:
A Deque is a linear data structure that allows insertion and deletion at both ends (front and rear).

Logic:
- Use a list to store elements.
- Support operations to add/remove elements from both front and rear.

Time Complexity:
- Insertion/Deletion at both ends: O(1) if using collections.deque, else O(n)

Space Complexity:
- O(n)
"""

from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def add_front(self, item):
        self.deque.appendleft(item)
        print(f"Added to front: {item}")

    def add_rear(self, item):
        self.deque.append(item)
        print(f"Added to rear: {item}")

    def remove_front(self):
        if not self.deque:
            print("Deque is empty.")
            return None
        item = self.deque.popleft()
        print(f"Removed from front: {item}")
        return item

    def remove_rear(self):
        if not self.deque:
            print("Deque is empty.")
            return None
        item = self.deque.pop()
        print(f"Removed from rear: {item}")
        return item

    def is_empty(self):
        return len(self.deque) ==0

    def peek_front(self):
        if not self.deque:
            print("Deque is empty.")
            return None
        return self.deque[0]

    def peek_rear(self):
        if not self.deque:
            print("Deque is empty.")
            return None
        return self.deque[-1]

    def display(self):
        print("Deque:", list(self.deque))

def main():
    dq = Deque()
    dq.add_rear(10)
    dq.add_front(20)
    dq.add_rear(30)
    dq.display()
    dq.remove_front()
    dq.display()
    dq.remove_rear()
    dq.display()
    print(f"Front element is {dq.peek_front()}")
    print(f"Rear element is {dq.peek_rear()}")

if __name__ == "__main__":
    main()
