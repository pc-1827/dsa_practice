"""
Huffman Coding

Description:
Huffman Coding is a compression algorithm used for lossless data compression. It assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.

Logic:
- Count the frequency of each character in the input.
- Create a priority queue (min-heap) where each node represents a character and its frequency.
- While there is more than one node in the queue:
    - Extract the two nodes with the lowest frequency.
    - Create a new internal node with these two nodes as children and frequency equal to the sum of their frequencies.
    - Insert the new node back into the priority queue.
- Assign binary codes to characters by traversing the Huffman tree.

Time Complexity:
- O(n log n), where n is the number of unique characters

Space Complexity:
- O(n) for storing the Huffman tree and codes
"""

import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # Define comparison operators for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(node1.freq + node2.freq, None, node1, node2)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text

def main():
    text = "this is an example for huffman encoding"
    print(f"Original text: {text}")

    encoded_text, codes = huffman_encoding(text)
    print(f"Encoded text: {encoded_text}")
    print("Huffman Codes:")
    for char, code in codes.items():
        print(f"'{char}': {code}")

    decoded_text = huffman_decoding(encoded_text, codes)
    print(f"Decoded text: {decoded_text}")

if __name__ == "__main__":
    main()
