"""
Binary Tree

Description:
A Binary Tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. It is used to implement binary search trees and binary heaps, and it serves as the foundation for more complex tree structures.

Logic:
- Each node contains data and references to its left and right child nodes.
- Traversal methods (in-order, pre-order, post-order) are used to navigate the tree.
- Insertion and deletion operations are performed by navigating the tree structure.

Time Complexity:
- Insertion: O(n)
- Deletion: O(n)
- Traversal: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert_left(self, current_node, data):
        if current_node.left is None:
            current_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, data):
        if current_node.right is None:
            current_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = current_node.right
            current_node.right = new_node

    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        return root

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=' ')
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=' ')

def main():
    bt = BinaryTree(1)
    bt.insert_left(bt.root, 2)
    bt.insert_right(bt.root, 3)
    bt.insert_left(bt.root.left, 4)
    bt.insert_right(bt.root.left, 5)

    print("In-order Traversal:")
    bt.inorder_traversal(bt.root)
    print("\nPre-order Traversal:")
    bt.preorder_traversal(bt.root)
    print("\nPost-order Traversal:")
    bt.postorder_traversal(bt.root)

    print("\n\nDeleting node 2:")
    bt.delete_node(bt.root, 2)
    print("In-order Traversal after deletion:")
    bt.inorder_traversal(bt.root)

if __name__ == "__main__":
    main()
