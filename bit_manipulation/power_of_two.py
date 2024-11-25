"""
Checking if a Number is a Power of 2

Description:
Determining whether a given number is a power of two by leveraging bitwise operations.

Logic:
- A number that is a power of two has exactly one set bit in its binary representation.
- Using the expression `n & (n -1)` will be zero only if `n` is a power of two.

Time Complexity:
- O(1)

Space Complexity:
- O(1)
"""

def is_power_of_two(n):
    if n <=0:
        return False
    return (n & (n -1)) ==0

def main():
    numbers = [1, 2, 3, 4, 5, 8, 16, 18]
    for num in numbers:
        result = is_power_of_two(num)
        print(f"{num} is a power of two: {result}")

if __name__ == "__main__":
    main()
