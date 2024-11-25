"""
Suffix Tree

Description:
A Suffix Tree is a compressed trie containing all the suffixes of a given string. It is used for various string processing algorithms like pattern matching, finding the longest repeated substring, and more.

Logic:
- Each edge represents a substring of the input string.
- All suffixes of the string are inserted into the tree.
- The tree allows for efficient pattern matching by traversing the tree based on the characters of the pattern.

Time Complexity:
- Building the tree: O(n)
- Pattern matching: O(m) where m is the length of the pattern
"""

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.indexes = []

class SuffixTree:
    def __init__(self, s):
        self.root = SuffixTreeNode()
        self.build_suffix_tree(s)

    def build_suffix_tree(self, s):
        for i in range(len(s)):
            current = self.root
            for char in s[i:]:
                if char not in current.children:
                    current.children[char] = SuffixTreeNode()
                current = current.children[char]
                current.indexes.append(i)

    def search(self, pattern):
        current = self.root
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]
        return current.indexes

def main():
    text = "bananabanaba"
    st = SuffixTree(text)

    patterns = ["ban", "ana", "naba", "apple"]
    for pattern in patterns:
        result = st.search(pattern)
        if result:
            print(f"Pattern '{pattern}' found at positions: {result}")
        else:
            print(f"Pattern '{pattern}' not found in the text.")

if __name__ == "__main__":
    main()
