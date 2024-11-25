"""
Kadane's Algorithm (Maximum Subarray Sum)

Description:
Kadane's Algorithm is used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

Logic:
- Initialize two variables, `max_current` and `max_global`, with the first element of the array.
- Iterate through the array starting from the second element.
- For each element, update `max_current` to be the maximum of the current element and the sum of `max_current` with the current element.
- Update `max_global` if `max_current` is greater than `max_global`.
- After completing the iteration, `max_global` will hold the maximum subarray sum.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

def kadane_algorithm(arr):
    if not arr:
        return 0
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

def main():
    arr = [34, -50, 42, 14, -5, 86]
    max_sum = kadane_algorithm(arr)
    print(f"Maximum subarray sum is {max_sum}")

if __name__ == "__main__":
    main()
