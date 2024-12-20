"""
AVL Tree

Description:
An AVL Tree is a self-balancing Binary Search Tree where the difference between heights of left and right subtrees cannot be more than one for all nodes. It ensures O(log n) time complexity for insertion, deletion, and search operations.

Logic:
- Each node stores its height.
- Perform rotations (left, right, left-right, right-left) to maintain the balance factor after insertions and deletions.
- Update heights after every insertion or deletion.

Time Complexity:
- Insertion: O(log n)
- Deletion: O(log n)
- Search: O(log n)
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right
        if balance >1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left
        if balance >1 and self.get_balance(root.left) >=0:
            return self.right_rotate(root)

        # Left Right
        if balance >1 and self.get_balance(root.left) <0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and self.get_balance(root.right) <=0:
            return self.left_rotate(root)

        # Right Left
        if balance < -1 and self.get_balance(root.right) >0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height =1 + max(self.get_height(z.left),
                          self.get_height(z.right))
        y.height =1 + max(self.get_height(y.left),
                          self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height =1 + max(self.get_height(z.left),
                          self.get_height(z.right))
        y.height =1 + max(self.get_height(y.left),
                          self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=' ')
            self.inorder_traversal(root.right)

def main():
    avl = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl.insert(root, key)

    print("In-order Traversal of AVL Tree:")
    avl.inorder_traversal(root)

    print("\n\nDeleting 40:")
    root = avl.delete(root, 40)
    print("In-order Traversal after deletion:")
    avl.inorder_traversal(root)

if __name__ == "__main__":
    main()
