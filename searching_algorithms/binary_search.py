"""
Binary Search Algorithm

Description:
Binary Search is an efficient search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.

Logic:
- Start with the entire array.
- Find the middle element.
- If the middle element is the target, return its index.
- If the target is less than the middle element, search the left subarray.
- If the target is greater, search the right subarray.
- Repeat until the target is found or the subarray size becomes zero.

Note: The array must be sorted before applying Binary Search.

Time Complexity:
- Best Case: O(1) (Target is the middle element)
- Average and Worst Case: O(log n)

Space Complexity:
- Iterative: O(1)
- Recursive: O(log n) due to recursion stack
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = sorted(arr)
    target = 23
    result = binary_search(sorted_arr, target)
    if result != -1:
        print(f"Element {target} found at index {result} in the sorted array.")
    else:
        print(f"Element {target} not found in the sorted array.")

if __name__ == "__main__":
    main()
