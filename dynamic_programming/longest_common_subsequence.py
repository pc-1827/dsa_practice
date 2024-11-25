"""
Longest Common Subsequence (LCS)

Description:
The Longest Common Subsequence problem involves finding the longest subsequence present in two sequences without changing the order of characters. It is a fundamental problem in computer science with applications in bioinformatics, text comparison, and more.

Logic:
- Use dynamic programming to build a matrix where each cell [i][j] represents the length of LCS of the first i characters of string1 and first j characters of string2.
- If characters match, increment the value from the previous diagonal cell.
- If they don't match, take the maximum value from the cell above or to the left.

Time Complexity:
- O(m * n), where m and n are the lengths of the two strings.

Space Complexity:
- O(m * n)
"""

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] +1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    # Reconstruct LCS
    lcs = []
    i, j = m, n
    while i >0 and j >0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -=1
            j -=1
        elif dp[i-1][j] > dp[i][j-1]:
            i -=1
        else:
            j -=1
    return ''.join(reversed(lcs))

def main():
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    lcs = longest_common_subsequence(s1, s2)
    print(f"Longest Common Subsequence of '{s1}' and '{s2}' is '{lcs}'")

if __name__ == "__main__":
    main()
