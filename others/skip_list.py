"""
Skip List Implementation

Description:
A Skip List is a probabilistic data structure that allows fast search, insertion, and deletion operations within an ordered sequence of elements. It consists of multiple levels where each level is a sorted linked list, and higher levels act as express lanes for lower levels.

Logic:
- Each node contains multiple forward pointers, one for each level it participates in.
- When inserting, randomly determine the level of the new node.
- Search and update operations traverse the levels from top to bottom for efficiency.

Time Complexity:
- Average case: O(log n) for search, insertion, and deletion.
- Worst case: O(n), but highly unlikely due to probabilistic balancing.
"""

import random

MAX_LEVEL = 16
P = 0.5

class SkipListNode:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level +1)

class SkipList:
    def __init__(self):
        self.header = SkipListNode(-1, MAX_LEVEL)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < P and lvl < MAX_LEVEL:
            lvl +=1
        return lvl

    def insert(self, key):
        update = [None] * (MAX_LEVEL +1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.key != key:
            lvl = self.random_level()
            if lvl > self.level:
                for i in range(self.level +1, lvl +1):
                    update[i] = self.header
                self.level = lvl
            new_node = SkipListNode(key, lvl)
            for i in range(lvl +1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return True
        return False

    def delete(self, key):
        update = [None] * (MAX_LEVEL +1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level +1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level >0 and self.header.forward[self.level] is None:
                self.level -=1

    def display_list(self):
        print("Skip List:")
        for i in range(self.level +1):
            current = self.header.forward[i]
            print(f"Level {i}: ", end='')
            while current:
                print(current.key, end=' ')
                current = current.forward[i]
            print()

def main():
    skip = SkipList()
    elements = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
    for elem in elements:
        skip.insert(elem)
    skip.display_list()

    search_keys = [19, 15]
    for key in search_keys:
        result = skip.search(key)
        print(f"Search for {key}: {'Found' if result else 'Not Found'}")

    skip.delete(19)
    print("\nAfter deleting 19:")
    skip.display_list()

    result = skip.search(19)
    print(f"Search for 19: {'Found' if result else 'Not Found'}")

if __name__ == "__main__":
    main()
