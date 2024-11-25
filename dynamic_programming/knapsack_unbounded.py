"""
Unbounded Knapsack Problem

Description:
The Unbounded Knapsack Problem is similar to the 0/1 Knapsack Problem, but here, an unlimited number of instances of each item is allowed. The goal is to maximize the total value without exceeding the knapsack capacity.

Logic:
- Use dynamic programming where dp[w] represents the maximum value achievable with weight w.
- For each weight, consider all items and update the dp array accordingly.

Time Complexity:
- O(n * W), where n is the number of items and W is the knapsack capacity.

Space Complexity:
- O(W)
"""

def knapsack_unbounded(weights, values, capacity):
    n = len(values)
    dp = [0]*(capacity +1)
    for w in range(capacity +1):
        for i in range(n):
            if weights[i] <=w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

def main():
    values = [10, 40, 50, 70]
    weights = [1, 3, 4, 5]
    capacity = 8
    max_value = knapsack_unbounded(weights, values, capacity)
    print(f"Maximum value in Unbounded Knapsack: {max_value}")

if __name__ == "__main__":
    main()
