"""
Bitwise Operations: AND, OR, XOR

Description:
Bitwise operations manipulate individual bits of integer operands. The primary bitwise operations are AND, OR, and XOR, each performing a specific logical operation between corresponding bits of two numbers.

Logic:
- AND (`&`): Sets each bit to 1 if both bits are 1.
- OR (`|`): Sets each bit to 1 if at least one of the bits is 1.
- XOR (`^`): Sets each bit to 1 if only one of the two bits is 1.

Time Complexity:
- O(1) for individual operations

Space Complexity:
- O(1)
"""

def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def bitwise_xor(a, b):
    return a ^ b

def main():
    a = 12  # 1100
    b = 10  # 1010
    print(f"{a} & {b} = {bitwise_and(a, b)}")  # 8 (1000)
    print(f"{a} | {b} = {bitwise_or(a, b)}")   # 14 (1110)
    print(f"{a} ^ {b} = {bitwise_xor(a, b)}")  # 6 (0110)

if __name__ == "__main__":
    main()
