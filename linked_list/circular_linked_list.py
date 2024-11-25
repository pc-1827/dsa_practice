"""
Circular Linked List Implementation

Description:
A Circular Linked List is a variation of a linked list where the last node points back to the first node, forming a circle. It allows efficient traversal from any point in the list.

Operations:
- Traversal
- Reversal
- Insertion at start, end, and specific position
- Deletion at start, end, and specific position

Time Complexity:
- Insertion/Deletion at start/end: O(1)
- Insertion/Deletion at specific position: O(n)
- Traversal: O(n)
- Reversal: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        current = self.head
        elements = []
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        print("Circular Linked List:", elements)

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            print(f"Inserted {data} as head.")
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        self.head = new_node
        current.next = self.head
        print(f"Inserted {data} at start.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            print(f"Inserted {data} as head.")
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        print(f"Inserted {data} at end.")

    def insert_after(self, prev_data, data):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        current = self.head
        while current.data != prev_data:
            current = current.next
            if current == self.head:
                print(f"Node with data {prev_data} not found.")
                return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} after {prev_data}.")

    def delete_at_start(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        if self.head.next == self.head:
            removed = self.head.data
            self.head = None
            print(f"Deleted {removed} from start.")
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        removed = self.head.data
        self.head = self.head.next
        current.next = self.head
        print(f"Deleted {removed} from start.")

    def delete_at_end(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        if self.head.next == self.head:
            removed = self.head.data
            self.head = None
            print(f"Deleted {removed} from end.")
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        removed = current.next.data
        current.next = self.head
        print(f"Deleted {removed} from end.")

    def delete_node(self, key):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        current = self.head
        prev = None
        while True:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    # Deleting head
                    if current.next == self.head:
                        self.head = None
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        self.head = current.next
                        temp.next = self.head
                print(f"Deleted {key} from the list.")
                return
            prev = current
            current = current.next
            if current == self.head:
                print(f"Node with data {key} not found.")
                return

    def reverse(self):
        if not self.head or self.head.next == self.head:
            print("Reversed the circular linked list.")
            return
        prev = None
        current = self.head
        next_node = None
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head.next = prev
        self.head = prev
        print("Reversed the circular linked list.")

def main():
    cll = CircularLinkedList()
    cll.insert_at_end(10)
    cll.insert_at_start(20)
    cll.insert_at_end(30)
    cll.insert_after(20,25)
    cll.traverse()
    cll.delete_node(25)
    cll.traverse()
    cll.delete_at_start()
    cll.traverse()
    cll.delete_at_end()
    cll.traverse()
    cll.insert_at_start(40)
    cll.insert_at_end(50)
    cll.traverse()
    cll.reverse()
    cll.traverse()

if __name__ == "__main__":
    main()
