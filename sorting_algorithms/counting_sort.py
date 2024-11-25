"""
Counting Sort Algorithm

Description:
Counting Sort is an integer sorting algorithm that operates by counting the number of objects that possess distinct key values. It is efficient for small ranges of input data.

Logic:
- Find the maximum and minimum values in the array to determine the range.
- Create a count array to store the frequency of each unique element.
- Modify the count array to store the cumulative count.
- Build the output array by placing elements at their correct positions.
- Handle negative numbers by adjusting the index based on the minimum value.

Time Complexity:
- Best, Average, and Worst Case: O(n + k) where k is the range of input

Space Complexity:
- O(n + k)
"""

def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element
    for number in arr:
        count[number - min_val] +=1

    # Update count[i] so that count[i] contains the actual position of this element in output
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Build the output array
    for number in reversed(arr):
        output[count[number - min_val] -1] = number
        count[number - min_val] -=1

    return output

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = counting_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
