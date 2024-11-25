"""
Aho-Corasick Algorithm

Description:
The Aho-Corasick Algorithm is used for searching multiple patterns simultaneously in a text. It constructs a trie of the patterns and augments it with failure links to allow efficient transitions when mismatches occur.

Logic:
- Build a trie from the given set of patterns.
- Construct failure links for each node in the trie to handle mismatches.
- Traverse the text character by character using the trie and failure links to find all pattern occurrences.
- Record the positions where patterns are matched.

Time Complexity:
- Preprocessing: O(m), where `m` is the total number of characters in all patterns
- Searching: O(n + k), where `n` is the length of the text and `k` is the number of matches

Space Complexity:
- O(m) for the trie and failure links
"""

from collections import deque, defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.failure = None
        self.output = []

def build_trie(patterns):
    root = TrieNode()
    for idx, pattern in enumerate(patterns):
        node = root
        for char in pattern:
            node = node.children.setdefault(char, TrieNode())
        node.output.append(idx)
    return root

def build_failure_links(root):
    queue = deque()
    for child in root.children.values():
        child.failure = root
        queue.append(child)

    while queue:
        current_node = queue.popleft()
        for char, child in current_node.children.items():
            failure_node = current_node.failure
            while failure_node and char not in failure_node.children:
                failure_node = failure_node.failure
            child.failure = failure_node.children[char] if failure_node and char in failure_node.children else root
            child.output += child.failure.output
            queue.append(child)

def aho_corasick_search(text, patterns):
    root = build_trie(patterns)
    build_failure_links(root)
    node = root
    occurrences = defaultdict(list)
    for index, char in enumerate(text):
        while node and char not in node.children:
            node = node.failure
        if not node:
            node = root
            continue
        node = node.children[char]
        for pattern_idx in node.output:
            occurrences[patterns[pattern_idx]].append(index - len(patterns[pattern_idx]) +1)
    return occurrences

def main():
    text = "ABABDABACDABABCABAB"
    patterns = ["ABABCABAB", "ABABD", "ACD", "BAB"]
    occurrences = aho_corasick_search(text, patterns)
    for pattern, indices in occurrences.items():
        print(f"Pattern '{pattern}' found at indices: {indices}")
        for index in indices:
            print(f"Match at index {index}: {text[index:index+len(pattern)]}")

if __name__ == "__main__":
    main()
