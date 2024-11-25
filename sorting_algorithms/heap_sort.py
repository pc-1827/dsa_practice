"""
Heap Sort Algorithm

Description:
Heap Sort is a comparison-based sorting technique based on a Binary Heap data structure. It divides the input into a sorted and an unsorted region and iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.

Logic:
- Build a max heap from the input data.
- Repeatedly extract the maximum element from the heap and place it at the end of the array.
- Reduce the heap size and heapify the root element to maintain the heap property.
- Continue until the heap size is reduced to one.

Time Complexity:
- Best, Average, and Worst Case: O(n log n)

Space Complexity:
- O(1) (In-place sorting)
"""

import heapq

def heap_sort(arr):
    heap = []
    for item in arr:
        heapq.heappush(heap, item)
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    return sorted_arr

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = heap_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
