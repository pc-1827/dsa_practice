"""
Singly Linked List Implementation

Description:
A Singly Linked List is a linear data structure where each element points to the next element. It allows efficient insertion and deletion from the beginning.

Operations:
- Traversal
- Reversal
- Insertion at start, end, and middle
- Deletion at start, end, and middle

Time Complexity:
- Insertion/Deletion at start: O(1)
- Insertion/Deletion at end: O(n)
- Traversal: O(n)
- Reversal: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
        current.next = new_node
        print(f"Inserted {data} after {prev_data}.")

    def delete_at_start(self):
        if not self.head:
            print("Linked List is empty.")
            return
        removed = self.head.data
        self.head = self.head.next
        print(f"Deleted {removed} from start.")

    def delete_at_end(self):
        if not self.head:
            print("Linked List is empty.")
            return
        if not self.head.next:
            removed = self.head.data
            self.head = None
            print(f"Deleted {removed} from end.")
            return
        current = self.head
        while current.next.next:
            current = current.next
        removed = current.next.data
        current.next = None
        print(f"Deleted {removed} from end.")

    def delete_node(self, key):
        if not self.head:
            print("Linked List is empty.")
            return
        if self.head.data == key:
            self.head = self.head.next
            print(f"Deleted {key} from list.")
            return
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        if current.next:
            removed = current.next.data
            current.next = current.next.next
            print(f"Deleted {removed} from list.")
        else:
            print(f"Node with data {key} not found.")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Reversed the linked list.")

def main():
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_start(20)
    sll.insert_at_end(30)
    sll.insert_after(20,25)
    sll.traverse()
    sll.delete_node(25)
    sll.traverse()
    sll.delete_at_start()
    sll.traverse()
    sll.delete_at_end()
    sll.traverse()
    sll.insert_at_start(40)
    sll.insert_at_end(50)
    sll.traverse()
    sll.reverse()
    sll.traverse()

if __name__ == "__main__":
    main()
