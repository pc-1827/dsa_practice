"""
Bloom Filter Implementation

Description:
A Bloom Filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It can yield false positives but never false negatives. It is widely used in scenarios where space is a constraint and some false positives are acceptable.

Logic:
- Initialize a bit array of size m and use k different hash functions.
- To add an element, hash it with all k functions and set the corresponding bits to 1.
- To check membership, hash the element with all k functions and verify that all corresponding bits are set to 1.
- If any bit is 0, the element is definitely not in the set. If all are 1, it might be in the set.

Time Complexity:
- Insertion: O(k)
- Query: O(k)
"""

import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        """
        Initialize the Bloom Filter.

        :param size: Size of the bit array.
        :param hash_count: Number of hash functions.
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = 0  # Using an integer to represent bits

    def _hashes(self, item):
        """Generate k hash values for the given item."""
        hashes = []
        for i in range(self.hash_count):
            hash_input = f"{item}_{i}".encode('utf-8')
            hash_digest = hashlib.md5(hash_input).hexdigest()
            hash_int = int(hash_digest, 16)
            hashes.append(hash_int % self.size)
        return hashes

    def add(self, item):
        """Add an item to the Bloom Filter."""
        for hash_val in self._hashes(item):
            self.bit_array |= 1 << hash_val

    def check(self, item):
        """Check if an item is in the Bloom Filter."""
        for hash_val in self._hashes(item):
            if not (self.bit_array & (1 << hash_val)):
                return False
        return True

def main():
    bloom = BloomFilter(size=1000, hash_count=5)
    elements = ["apple", "banana", "orange", "grape", "mango"]
    for elem in elements:
        bloom.add(elem)

    test_elements = ["apple", "banana", "cherry", "date", "fig"]
    for elem in test_elements:
        result = bloom.check(elem)
        print(f"Element '{elem}' is {'probably in' if result else 'not in'} the Bloom Filter.")

if __name__ == "__main__":
    main()
