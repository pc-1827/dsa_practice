"""
Longest Increasing Subsequence (LIS)

Description:
The Longest Increasing Subsequence problem involves finding the longest subsequence of a given sequence where the elements are in increasing order. It is widely used in various applications like data analysis and pattern recognition.

Logic:
- Use dynamic programming where each position i in the array stores the length of the LIS ending at that position.
- For each element, check all previous elements and update the LIS length accordingly.
- Optionally, track the actual subsequence by storing predecessors.

Time Complexity:
- O(n^2), where n is the length of the array.

Space Complexity:
- O(n)
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1]*n
    predecessor = [-1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] +1 > dp[i]:
                dp[i] = dp[j] +1
                predecessor[i] = j
    # Find the maximum value in dp and its index
    max_len = max(dp)
    index = dp.index(max_len)
    # Reconstruct LIS
    lis = []
    while index != -1:
        lis.append(arr[index])
        index = predecessor[index]
    return lis[::-1]

def main():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    lis = longest_increasing_subsequence(arr)
    print(f"Longest Increasing Subsequence is {lis}")

if __name__ == "__main__":
    main()
