"""
Insertion Sort Algorithm

Description:
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms but has performance advantages for small or mostly sorted datasets.

Logic:
- Iterate from the second element to the end of the array.
- For each element, compare it with elements in the sorted sublist to its left.
- Shift all larger elements one position to the right to make space.
- Insert the current element into its correct position.

Time Complexity:
- Best Case: O(n) (When the array is already sorted)
- Average and Worst Case: O(n^2)

Space Complexity:
- O(1) (In-place sorting)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = insertion_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
