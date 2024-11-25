"""
Merge Sort Algorithm

Description:
Merge Sort is a divide and conquer algorithm that divides the array into halves, sorts each half, and then merges the sorted halves to produce the sorted array.

Logic:
- If the array has more than one element, divide it into two halves.
- Recursively sort each half.
- Merge the two sorted halves into a single sorted array.

Time Complexity:
- Best, Average, and Worst Case: O(n log n)

Space Complexity:
- O(n) due to the temporary arrays used for merging
"""

def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        # Recursively sort both halves
        merge_sort(L)
        merge_sort(R)

        i = j = k =0

        # Merge the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j +=1
            k +=1

        # Copy any remaining elements of L
        while i < len(L):
            arr[k] = L[i]
            i +=1
            k +=1

        # Copy any remaining elements of R
        while j < len(R):
            arr[k] = R[j]
            j +=1
            k +=1
    return arr

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = merge_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
