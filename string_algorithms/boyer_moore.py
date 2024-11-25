"""
Boyer-Moore Algorithm

Description:
The Boyer-Moore Algorithm is a highly efficient string searching algorithm that preprocesses the pattern to create bad character and good suffix heuristics, allowing it to skip sections of the text, thus reducing the number of comparisons.

Logic:
- Preprocess the pattern to create:
    - Bad Character Table: Indicates how far to shift the pattern when a mismatch occurs based on the mismatched character.
    - Good Suffix Table: Indicates how far to shift the pattern when a mismatch occurs based on the matched suffix.
- Start matching from the end of the pattern:
    - If a mismatch occurs, use the heuristics to determine the shift distance.
    - If all characters match, record the match and shift the pattern based on the good suffix table.
- Continue until the pattern exceeds the text length.

Time Complexity:
- Best Case: O(n/m)
- Average and Worst Case: O(n + m)

Space Complexity:
- O(m + |\Sigma|), where |\Sigma| is the size of the alphabet
"""

def bad_character_table(pattern):
    table = {}
    length = len(pattern)
    for i in range(length):
        table[pattern[i]] = i
    return table

def good_suffix_table(pattern):
    length = len(pattern)
    table = [0]*length
    last_prefix_position = length

    for i in range(length-1, -1, -1):
        if is_prefix(pattern, i +1):
            last_prefix_position = i +1
        table[length -1 -i] = last_prefix_position -i + length -1

    for i in range(1, length):
        slen = suffix_length(pattern, i)
        if pattern[i - slen] != pattern[length -1 -slen]:
            table[slen] = length -1 -slen + slen
    return table

def is_prefix(pattern, p):
    length = len(pattern)
    suffix = pattern[p:length]
    prefix = pattern[0:length -p]
    return suffix == prefix

def suffix_length(pattern, p):
    length = len(pattern)
    i =0
    while (p -i -1 >=0) and (pattern[p -i -1] == pattern[length -i -1]):
        i +=1
    return i

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m ==0:
        return []
    bad_char = bad_character_table(pattern)
    good_suffix = good_suffix_table(pattern)
    matches = []
    s =0
    while s <= n -m:
        j = m -1
        while j >=0 and pattern[j] == text[s +j]:
            j -=1
        if j <0:
            matches.append(s)
            s += good_suffix[0] if m >1 else 1
        else:
            bc_shift = j - bad_char.get(text[s +j], -1)
            gs_shift = good_suffix[m -1 -j] if (m -1 -j) < m else 1
            s += max(1, max(bc_shift, gs_shift))
    return matches

def main():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = boyer_moore_search(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {matches}")
    for index in matches:
        print(f"Match at index {index}: {text[index:index+len(pattern)]}")

if __name__ == "__main__":
    main()
