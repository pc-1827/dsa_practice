"""
Coin Change Problem

Description:
The Coin Change Problem involves finding the minimum number of coins required to make a certain amount of change given unlimited supply of coins of specified denominations. It can also be modified to count the number of ways to make change.

Logic:
- Use dynamic programming to build a table where each entry dp[i] represents the minimum number of coins needed for amount i.
- Iterate through all amounts from 1 to target and update the dp table based on available coin denominations.

Time Complexity:
- O(n * m), where n is the amount and m is the number of coin denominations.

Space Complexity:
- O(n)
"""

def coin_change_min_coins(coins, amount):
    dp = [float('inf')]*(amount +1)
    dp[0] =0
    for coin in coins:
        for x in range(coin, amount +1):
            if dp[x - coin] +1 < dp[x]:
                dp[x] = dp[x - coin] +1
    return dp[amount] if dp[amount] != float('inf') else -1

def main():
    coins = [1, 2, 5]
    amount = 11
    min_coins = coin_change_min_coins(coins, amount)
    if min_coins != -1:
        print(f"Minimum number of coins to make {amount}: {min_coins}")
    else:
        print(f"Cannot make change for {amount} with given coins.")

if __name__ == "__main__":
    main()
