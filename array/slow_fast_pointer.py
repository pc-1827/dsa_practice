"""
Slow and Fast Pointer Technique

Description:
Slow and Fast Pointer Technique uses two pointers moving at different speeds to solve problems related to linked lists and arrays, such as cycle detection or finding the middle element.

Logic:
- Initialize two pointers, `slow` and `fast`.
- Move `slow` by one step and `fast` by two steps.
- Continue until `fast` reaches the end.
- If `slow` and `fast` meet, a cycle exists.

Example Implemented: Detect Cycle in a Linked List

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def main():
    # Creating a linked list with a cycle
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle here

    print("Cycle detected:" if has_cycle(node1) else "No cycle detected.")

if __name__ == "__main__":
    main()
