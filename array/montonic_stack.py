"""
Monotonic Stack

Description:
A Monotonic Stack is a stack that maintains its elements in a specific order (either increasing or decreasing). It is used to solve problems like finding the next greater or smaller element.

Logic:
- Iterate through the array.
- While the stack is not empty and the current element violates the monotonic condition, pop from the stack.
- The popped element's next greater/smaller element is the current element.
- Push the current element onto the stack.

Example Implemented: Next Greater Element

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

def next_greater_elements(arr):
    result = [-1]*len(arr)
    stack = []
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            index = stack.pop()
            result[index] = num
        stack.append(i)
    return result

def main():
    arr = [4, 5, 2, 25]
    result = next_greater_elements(arr)
    print("Next Greater Elements:", result)

if __name__ == "__main__":
    main()
