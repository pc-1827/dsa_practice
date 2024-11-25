"""
Rabin-Karp Algorithm

Description:
The Rabin-Karp Algorithm is a string searching algorithm that uses hashing to find any one of a set of pattern strings in a text. It is efficient for multiple pattern searches.

Logic:
- Compute the hash of the pattern and the hash of the first window of the text.
- Slide the window over the text one character at a time:
    - If the hash of the current window matches the pattern's hash, perform a character-by-character comparison to confirm the match.
    - Recompute the hash for the next window using a rolling hash technique to maintain efficiency.
- Record all positions where the pattern matches the text.

Time Complexity:
- Average Case: O(n + m)
- Worst Case: O(nm) due to hash collisions

Space Complexity:
- O(1)
"""

def rabin_karp(text, pattern, q=101):
    d = 256  # Number of characters in the input alphabet
    n = len(text)
    m = len(pattern)
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1

    # The value of h would be "pow(d, m-1)%q"
    for _ in range(m-1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m +1):
        # Check the hash values
        if p == t:
            # Check for characters one by one
            if text[i:i+m] == pattern:
                print(f"Pattern found at index {i}")

        # Calculate hash for next window
        if i < n - m:
            t = (d*(t - ord(text[i]) * h) + ord(text[i +m])) % q
            # We might get negative value of t, converting it to positive
            if t <0:
                t += q

def main():
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    print(f"Searching for pattern '{pattern}' in text '{text}':")
    rabin_karp(text, pattern)

if __name__ == "__main__":
    main()
