"""
Bubble Sort Algorithm

Description:
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

Logic:
- Traverse the array multiple times.
- In each traversal, compare adjacent elements and swap them if needed.
- After each pass, the largest unsorted element "bubbles" to its correct position.
- Optimization: If no swaps occur in a pass, the array is already sorted.

Time Complexity:
- Best Case: O(n) (When the array is already sorted)
- Average and Worst Case: O(n^2)

Space Complexity:
- O(1) (In-place sorting)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = bubble_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
