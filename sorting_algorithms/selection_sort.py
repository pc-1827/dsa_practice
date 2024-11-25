"""
Selection Sort Algorithm

Description:
Selection Sort is an in-place comparison sorting algorithm that divides the input list into two parts: a sorted sublist and an unsorted sublist. It repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the end of the sorted sublist.

Logic:
- Iterate over the array.
- For each position, find the minimum element in the unsorted portion.
- Swap the found minimum element with the first element of the unsorted portion.
- Repeat until the entire array is sorted.

Time Complexity:
- Best, Average, and Worst Case: O(n^2)

Space Complexity:
- O(1) (In-place sorting)
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = selection_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
