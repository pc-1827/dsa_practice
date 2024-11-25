"""
Two Pointer Technique

Description:
The Two Pointer Technique uses two pointers to iterate through the data structure, often used to solve problems involving pairs or subsets that satisfy certain conditions.

Logic:
- Initialize two pointers, typically starting at different ends or positions.
- Move the pointers towards each other or in a specific pattern based on the problem's requirements.
- Perform operations or checks as the pointers move to find the desired outcome.

Example Implemented: Container With Most Water

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

def max_area(height):
    left, right = 0, len(height) -1
    max_area = 0
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left +=1
        else:
            right -=1
    return max_area

def main():
    height = [1,8,6,2,5,4,8,3,7]
    result = max_area(height)
    print(f"Maximum area is {result}")

if __name__ == "__main__":
    main()
