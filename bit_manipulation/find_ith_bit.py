"""
Finding the ith Bit

Description:
Finding the ith bit of an integer involves checking whether the bit at the specified position is set (1) or not (0).

Logic:
- Create a mask by shifting 1 to the left by (i-1) positions.
- Perform a bitwise AND between the number and the mask.
- If the result is non-zero, the ith bit is set; otherwise, it's not.

Time Complexity:
- O(1)

Space Complexity:
- O(1)
"""

def find_ith_bit(n, i):
    mask = 1 << (i -1)
    return 1 if (n & mask) else 0

def main():
    number = 10  # 1010
    position = 3
    bit = find_ith_bit(number, position)
    print(f"The {position}th bit of {number} is {bit}")

if __name__ == "__main__":
    main()
