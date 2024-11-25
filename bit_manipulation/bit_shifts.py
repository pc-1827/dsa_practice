"""
Bit Shifts

Description:
Bit shifting operations move bits of an integer left or right, effectively multiplying or dividing the number by powers of two.

Logic:
- Left Shift (`<<`): Shifts bits to the left, equivalent to multiplying by 2^n.
- Right Shift (`>>`): Shifts bits to the right, equivalent to dividing by 2^n.

Time Complexity:
- O(1) for individual operations

Space Complexity:
- O(1)
"""

def left_shift(a, n):
    return a << n

def right_shift(a, n):
    return a >> n

def main():
    a = 5  # 0101
    print(f"{a} << 1 = {left_shift(a, 1)}")  # 10
    print(f"{a} << 2 = {left_shift(a, 2)}")  # 20
    print(f"{a} >> 1 = {right_shift(a, 1)}") # 2
    print(f"{a} >> 2 = {right_shift(a, 2)}") # 1

if __name__ == "__main__":
    main()
