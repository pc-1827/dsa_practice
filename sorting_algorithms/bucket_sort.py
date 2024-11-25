"""
Bucket Sort Algorithm

Description:
Bucket Sort is a distribution sort algorithm that divides the input array into a number of buckets, distributes the elements into these buckets, sorts each bucket individually, and then concatenates them to form the sorted array. It is particularly effective when the input is uniformly distributed over a range.

Logic:
- Determine the minimum and maximum values to calculate the range.
- Create buckets and distribute the elements into these buckets based on their value.
- Sort each individual bucket using a different sorting algorithm (e.g., Insertion Sort).
- Concatenate all sorted buckets to form the final sorted array.

Time Complexity:
- Best and Average Case: O(n + k)
- Worst Case: O(n^2) (when all elements are placed in a single bucket)

Space Complexity:
- O(n + k) where k is the number of buckets
"""

def bucket_sort(arr):
    if not arr:
        return arr
    bucket_count = len(arr)
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / bucket_count + 1

    # Create empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate all buckets into sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    sorted_arr = bucket_sort(arr.copy())
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
