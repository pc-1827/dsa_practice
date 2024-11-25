"""
Palindromic Substrings

Description:
The Palindromic Substrings problem involves finding all substrings of a given string that are palindromes. A palindrome is a string that reads the same backward as forward.

Logic:
- Use dynamic programming to build a table where dp[i][j] is True if the substring from index i to j is a palindrome.
- Every single character is a palindrome. Check for two characters and then extend to longer substrings.

Time Complexity:
- O(n^2), where n is the length of the string.

Space Complexity:
- O(n^2)
"""

def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    count =0
    for i in range(n):
        dp[i][i] = True
        count +=1
    for i in range(n -1):
        if s[i] == s[i +1]:
            dp[i][i +1] = True
            count +=1
    for length in range(3, n +1):
        for i in range(n - length +1):
            j = i + length -1
            if s[i] == s[j] and dp[i +1][j -1]:
                dp[i][j] = True
                count +=1
    return count

def main():
    s = "aaa"
    count = count_palindromic_substrings(s)
    print(f"Number of palindromic substrings in '{s}': {count}")

if __name__ == "__main__":
    main()
