"""
Quick Sort Algorithm

Description:
Quick Sort is an efficient, divide and conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two subarrays, according to whether they are less than or greater than the pivot.

Logic:
- Choose a pivot element (commonly the middle element).
- Partition the array into two subarrays:
    - Elements less than the pivot.
    - Elements equal to the pivot.
    - Elements greater than the pivot.
- Recursively apply Quick Sort to the subarrays.
- Concatenate the sorted subarrays and pivot elements.

Time Complexity:
- Best and Average Case: O(n log n)
- Worst Case: O(n^2) (when the smallest or largest element is always chosen as the pivot)

Space Complexity:
- O(log n) due to recursion stack
"""

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = quick_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
