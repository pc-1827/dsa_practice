"""
KMP Algorithm (Knuth-Morris-Pratt)

Description:
The KMP Algorithm is used for efficient pattern matching in strings. It avoids re-examining characters by utilizing a precomputed longest prefix suffix (LPS) array.

Logic:
- Preprocess the pattern to create the LPS array which indicates the longest proper prefix which is also a suffix.
- Traverse the text and pattern:
    - If characters match, move both pointers.
    - If there's a mismatch, use the LPS array to skip unnecessary comparisons.
    - Record the positions where the pattern matches the text.

Time Complexity:
- O(n + m), where `n` is the length of text and `m` is the length of pattern

Space Complexity:
- O(m) for the LPS array
"""

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length =0
    i =1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length +=1
            lps[i] = length
            i +=1
        else:
            if length !=0:
                length = lps[length -1]
            else:
                lps[i] =0
                i +=1
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j =0
    matches = []
    while i < len(text):
        if pattern[j] == text[i]:
            i +=1
            j +=1
        if j == len(pattern):
            matches.append(i -j)
            j = lps[j -1]
        elif i < len(text) and pattern[j] != text[i]:
            if j !=0:
                j = lps[j -1]
            else:
                i +=1
    return matches

def main():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(text, pattern)
    print(f"Pattern found at indices: {matches}")
    for index in matches:
        print(f"Match at index {index}: {text[index:index+len(pattern)]}")

if __name__ == "__main__":
    main()
