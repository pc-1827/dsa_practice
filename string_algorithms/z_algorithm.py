"""
Z Algorithm

Description:
The Z Algorithm is used for pattern searching in strings. It creates a Z-array that represents the length of the longest substring starting from each position which is also a prefix of the string. This helps in finding pattern occurrences efficiently.

Logic:
- Concatenate the pattern, a special character (not present in the string), and the text.
- Compute the Z-array for the concatenated string.
- Whenever a Z-value equals the length of the pattern, a match is found.
- The positions can be derived from the Z-array indices.

Time Complexity:
- O(n + m), where `n` is the length of the text and `m` is the length of the pattern

Space Complexity:
- O(n + m) for the Z-array
"""

def z_algorithm(s):
    n = len(s)
    z = [0]*n
    l, r =0,0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r -i +1, z[i -l])
        while i + z[i] <n and s[z[i]] == s[i + z[i]]:
            z[i] +=1
        if i + z[i] -1 >r:
            l, r = i, i + z[i] -1
    return z

def z_search(text, pattern):
    concat = pattern + "$" + text
    z = z_algorithm(concat)
    matches = []
    m = len(pattern)
    for i in range(m +1, len(z)):
        if z[i] == m:
            matches.append(i - m -1)
    return matches

def main():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = z_search(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {matches}")
    for index in matches:
        print(f"Match at index {index}: {text[index:index+len(pattern)]}")

if __name__ == "__main__":
    main()
