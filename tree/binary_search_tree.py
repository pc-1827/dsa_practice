"""
Binary Search Tree (BST)

Description:
A Binary Search Tree is a binary tree where each node has a comparable key (and associated value) and satisfies the property that the key in any node is greater than the keys in all nodes in that node's left subtree and less than those in its right subtree.

Logic:
- Insertion: Compare the key to be inserted with the root and recursively insert it into the left or right subtree.
- Deletion: Remove a node by replacing it with its in-order predecessor or successor.
- Traversal methods (in-order, pre-order, post-order) are used to navigate the tree.

Time Complexity:
- Insertion: O(h) where h is the height of the tree
- Deletion: O(h)
- Traversal: O(n)
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=' ')
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.key, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.key, end=' ')

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
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
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        return root

def main():
    bst = BinarySearchTree()
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    for key in keys:
        root = bst.insert(root, key)

    print("In-order Traversal:")
    bst.inorder_traversal(root)
    print("\nPre-order Traversal:")
    bst.preorder_traversal(root)
    print("\nPost-order Traversal:")
    bst.postorder_traversal(root)

    print("\n\nDeleting 20:")
    root = bst.delete_node(root, 20)
    print("In-order Traversal after deletion:")
    bst.inorder_traversal(root)

    print("\nDeleting 30:")
    root = bst.delete_node(root, 30)
    print("In-order Traversal after deletion:")
    bst.inorder_traversal(root)

    print("\nDeleting 50:")
    root = bst.delete_node(root, 50)
    print("In-order Traversal after deletion:")
    bst.inorder_traversal(root)

if __name__ == "__main__":
    main()
