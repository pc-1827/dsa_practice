"""
Trie (Prefix Tree)

Description:
A Trie, also known as a Prefix Tree, is a tree-like data structure used to efficiently store and retrieve keys in a dataset of strings. It is commonly used for autocomplete and spell checking.

Logic:
- Each node represents a character of a string.
- Insertion involves adding nodes for each character in the string.
- Search traverses the tree based on the characters of the string.

Time Complexity:
- Insertion: O(m) where m is the length of the string
- Search: O(m)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

def main():
    trie = Trie()
    words = ["apple", "app", "application", "apt", "bat", "batch", "baton"]
    for word in words:
        trie.insert(word)

    search_words = ["app", "apple", "apex", "bat", "bath"]
    for word in search_words:
        result = trie.search(word)
        print(f"Search for '{word}': {'Found' if result else 'Not Found'}")

    prefixes = ["ap", "bat", "ba", "cat"]
    for prefix in prefixes:
        result = trie.starts_with(prefix)
        print(f"Starts with '{prefix}': {'Yes' if result else 'No'}")

if __name__ == "__main__":
    main()
