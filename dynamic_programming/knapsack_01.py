"""
0/1 Knapsack Problem

Description:
The 0/1 Knapsack Problem is a classic optimization problem where, given a set of items each with a weight and value, the goal is to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is maximized. Each item can be included at most once.

Logic:
- Use dynamic programming to build a table where each entry dp[i][w] represents the maximum value achievable with the first i items and a weight limit w.
- For each item, decide to include it or not based on maximum value.

Time Complexity:
- O(n * W), where n is the number of items and W is the knapsack capacity.

Space Complexity:
- O(n * W)
"""

def knapsack_01(weights, values, capacity):
    n = len(values)
    dp = [[0]*(capacity +1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity +1):
            if weights[i-1] <=w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

def main():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_value = knapsack_01(weights, values, capacity)
    print(f"Maximum value in 0/1 Knapsack: {max_value}")

if __name__ == "__main__":
    main()
