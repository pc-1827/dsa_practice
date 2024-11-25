"""
Sliding Window Technique

Description:
Sliding Window Technique is used to solve problems that involve finding a subarray or substring that satisfies certain conditions. It optimizes the solution by maintaining a window that slides over the data structure.

Logic:
- Initialize two pointers, `left` and `right`, to define the window boundaries.
- Move the `right` pointer to expand the window until the condition is met.
- Once the condition is met, move the `left` pointer to shrink the window and find the optimal solution.
- Continue this process until the end of the array is reached.

Example Implemented: Minimum Window Substring

Time Complexity:
- O(n)

Space Complexity:
- O(k) where k is the number of unique characters
"""

def min_window_substring(s, t):
    from collections import Counter
    dict_t = Counter(t)
    required = len(dict_t)
    left, right = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while right < len(s):
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) +1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed +=1

        while left <= right and formed == required:
            character = s[left]
            if right - left +1 < ans[0]:
                ans = (right - left +1, left, right)
            window_counts[character] -=1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -=1
            left +=1
        right +=1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]

def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    result = min_window_substring(s, t)
    print(f"Minimum window substring is '{result}'")

if __name__ == "__main__":
    main()
