"""
Edit Distance (Levenshtein Distance)

Description:
The Edit Distance problem involves finding the minimum number of operations required to convert one string into another. The allowed operations are insertion, deletion, and substitution of a single character.

Logic:
- Use dynamic programming to build a matrix where each cell dp[i][j] represents the minimum edit distance between the first i characters of word1 and the first j characters of word2.
- Calculate the cost based on whether characters match or not and choose the minimum among insertion, deletion, and substitution.

Time Complexity:
- O(m * n), where m and n are the lengths of the two strings.

Space Complexity:
- O(m * n)
"""

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n +1) for _ in range(m +1)]
    for i in range(m +1):
        dp[i][0] =i
    for j in range(n +1):
        dp[0][j] =j
    for i in range(1, m +1):
        for j in range(1, n +1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] =1 + min(dp[i-1][j],    # Deletion
                                   dp[i][j-1],    # Insertion
                                   dp[i-1][j-1])  # Substitution
    return dp[m][n]

def main():
    word1 = "intention"
    word2 = "execution"
    distance = edit_distance(word1, word2)
    print(f"Edit Distance between '{word1}' and '{word2}': {distance}")

if __name__ == "__main__":
    main()
