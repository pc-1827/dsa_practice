"""
Matrix Chain Multiplication

Description:
The Matrix Chain Multiplication problem involves finding the most efficient way to multiply a given sequence of matrices. The objective is to determine the order of matrix multiplications that minimizes the total number of scalar multiplications.

Logic:
- Use dynamic programming to build a table where each entry dp[i][j] represents the minimum number of multiplications needed to compute the product of matrices from index i to j.
- Consider all possible splitting points and choose the one that gives the minimum cost.

Time Complexity:
- O(n^3), where n is the number of matrices.

Space Complexity:
- O(n^2)
"""

def matrix_chain_order(p):
    n = len(p) -1
    dp = [[0]*n for _ in range(n)]
    for length in range(2, n +1):
        for i in range(n - length +1):
            j = i + length -1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k +1][j] + p[i]*p[k +1]*p[j +1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n -1]

def main():
    # Matrix dimensions: A1 (10x30), A2 (30x5), A3 (5x60)
    p = [10, 30, 5, 60]
    min_cost = matrix_chain_order(p)
    print(f"Minimum number of multiplications needed: {min_cost}")

if __name__ == "__main__":
    main()
