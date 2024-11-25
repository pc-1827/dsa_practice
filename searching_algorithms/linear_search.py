"""
Linear Search Algorithm

Description:
Linear Search is a straightforward search algorithm that checks each element of the array sequentially until the target element is found or the list ends.

Logic:
- Iterate through each element in the array.
- Compare the current element with the target.
- If a match is found, return the index.
- If no match is found after traversing the entire array, return -1.

Time Complexity:
- Best Case: O(1) (Target is the first element)
- Average and Worst Case: O(n)

Space Complexity:
- O(1) (Constant space)
"""

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def main():
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 78, 0, 45, 23, 67, 89, 12, 54, 33, 21, 9, 10]
    target = 23
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found.")

if __name__ == "__main__":
    main()
