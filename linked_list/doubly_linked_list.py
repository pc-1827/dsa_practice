"""
Doubly Linked List Implementation

Description:
A Doubly Linked List is a linear data structure where each node has pointers to both the next and previous nodes. It allows efficient insertion and deletion from both ends.

Operations:
- Traversal (forward and backward)
- Reversal
- Insertion at start, end, and middle
- Deletion at start, end, and middle

Time Complexity:
- Insertion/Deletion at start/end: O(1)
- Insertion/Deletion at middle: O(n)
- Traversal: O(n)
- Reversal: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Doubly Linked List (Forward):", elements)

    def traverse_backward(self):
        current = self.head
        if not current:
            print("Doubly Linked List is empty.")
            return
        while current.next:
            current = current.next
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev
        print("Doubly Linked List (Backward):", elements)

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        print(f"Inserted {data} at start.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} as head.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"Inserted {data} at end.")

    def insert_after(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        print(f"Inserted {data} after {prev_data}.")

    def delete_at_start(self):
        if not self.head:
            print("Doubly Linked List is empty.")
            return
        removed = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        print(f"Deleted {removed} from start.")

    def delete_at_end(self):
        if not self.head:
            print("Doubly Linked List is empty.")
            return
        current = self.head
        if not current.next:
            removed = current.data
            self.head = None
            print(f"Deleted {removed} from end.")
            return
        while current.next:
            current = current.next
        removed = current.data
        current.prev.next = None
        print(f"Deleted {removed} from end.")

    def delete_node(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if not current:
            print(f"Node with data {key} not found.")
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        print(f"Deleted {key} from the list.")

    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev
        print("Reversed the doubly linked list.")

def main():
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_start(20)
    dll.insert_at_end(30)
    dll.insert_after(20,25)
    dll.traverse_forward()
    dll.traverse_backward()
    dll.delete_node(25)
    dll.traverse_forward()
    dll.delete_at_start()
    dll.traverse_forward()
    dll.delete_at_end()
    dll.traverse_forward()
    dll.insert_at_start(40)
    dll.insert_at_end(50)
    dll.traverse_forward()
    dll.traverse_backward()
    dll.reverse()
    dll.traverse_forward()
    dll.traverse_backward()

if __name__ == "__main__":
    main()
