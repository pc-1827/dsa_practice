"""
Suffix Array

Description:
A Suffix Array is an array that contains the starting indices of all suffixes of a string in sorted order. It is used in various string processing algorithms.

Logic:
- Generate all possible suffixes of the given string along with their starting indices.
- Sort the suffixes lexicographically.
- Extract and return the starting indices from the sorted suffixes.

Time Complexity:
- O(n log n) due to sorting

Space Complexity:
- O(n^2) due to storing all suffixes
"""

def build_suffix_array(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def main():
    s = "banana"
    suffix_array = build_suffix_array(s)
    print("Suffix Array:", suffix_array)
    print("Sorted Suffixes:")
    for index in suffix_array:
        print(s[index:])

if __name__ == "__main__":
    main()
