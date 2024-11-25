"""
Subset Sum Problem

Description:
The Subset Sum Problem is to determine if there is a subset of a given set with a sum equal to a given target. It is a fundamental problem in computer science, particularly in the fields of combinatorics and cryptography.

Logic:
- Use dynamic programming to build a table where dp[i][j] is True if a subset of the first i numbers has a sum equal to j.
- Fill the table by considering whether to include each number in the subset.

Time Complexity:
- O(n * sum), where n is the number of elements and sum is the target sum.

Space Complexity:
- O(n * sum)
"""

def subset_sum(nums, target):
    n = len(nums)
    dp = [[False]*(target +1) for _ in range(n +1)]
    for i in range(n +1):
        dp[i][0] = True
    for i in range(1, n +1):
        for j in range(1, target +1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
    return dp[n][target]

def main():
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    if subset_sum(nums, target):
        print(f"A subset with sum {target} exists.")
    else:
        print(f"No subset with sum {target} exists.")

if __name__ == "__main__":
    main()
