"""
Rod Cutting Problem

Description:
The Rod Cutting Problem involves cutting a rod into smaller lengths to maximize the total profit based on given prices for each possible length. It is a classic example of optimization using dynamic programming.

Logic:
- Use dynamic programming to determine the maximum revenue obtainable by cutting up the rod and selling the pieces.
- Consider all possible first cuts and choose the one that yields the maximum profit.

Time Complexity:
- O(n^2), where n is the length of the rod.

Space Complexity:
- O(n)
"""

def rod_cutting(prices, n):
    dp = [0]*(n +1)
    for i in range(1, n +1):
        max_val = -float('inf')
        for j in range(1, i +1):
            max_val = max(max_val, prices[j-1] + dp[i -j])
        dp[i] = max_val
    return dp[n]

def main():
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 8
    max_revenue = rod_cutting(prices, n)
    print(f"Maximum revenue obtainable: {max_revenue}")

if __name__ == "__main__":
    main()
