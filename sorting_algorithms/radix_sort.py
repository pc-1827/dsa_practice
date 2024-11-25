"""
Radix Sort Algorithm

Description:
Radix Sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by individual digits which share the same significant position and value.

Logic:
- Find the maximum number to determine the number of digits.
- Perform counting sort for each digit, starting from the least significant digit to the most significant digit.
- Use a stable sort (like Counting Sort) to sort based on the current digit.

Time Complexity:
- O(d*(n + k)) where d is the number of digits and k is the base of the number system

Space Complexity:
- O(n + k)
"""

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10

    # Store the count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[ index % 10 ] +=1

    # Change count[i] so that count[i] contains the actual position of this digit in output[]
    for i in range(1,10):
        count[i] += count[i-1]

    # Build the output array
    for i in range(n-1, -1, -1):
        index = arr[i] // exp
        output[count[ index %10 ] -1] = arr[i]
        count[ index %10 ] -=1

    # Copy the output array to arr[], so that arr contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp =1
    while max_val // exp >0:
        counting_sort_for_radix(arr, exp)
        exp *=10
    return arr

def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66, 34, 7, 23, 32, 5, 62, 32, 78, 0, 45, 89, 12]
    sorted_arr = radix_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
