"""
Prefix Sum Array

Description:
A Prefix Sum Array stores the cumulative sum of elements up to each index in the array, allowing for efficient range sum queries.

Logic:
- Initialize a prefix sum array with the first element being the first element of the original array.
- Iterate through the original array, adding the current element to the last element of the prefix sum array and appending it.
- To find the sum of a range [i, j], calculate prefix_sum[j] - prefix_sum[i-1].

Time Complexity:
- Building Prefix Sum: O(n)
- Range Sum Query: O(1)

Space Complexity:
- O(n)
"""

def build_prefix_sum(arr):
    prefix_sum = [0]*len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum

def range_sum(prefix_sum, i, j):
    if i == 0:
        return prefix_sum[j]
    return prefix_sum[j] - prefix_sum[i-1]

def main():
    arr = [3, 2, 4, 5, 1, 6, 7]
    prefix_sum = build_prefix_sum(arr)
    print("Prefix Sum Array:", prefix_sum)
    print(f"Sum of range [2,5] is {range_sum(prefix_sum, 2,5)}")

if __name__ == "__main__":
    main()
