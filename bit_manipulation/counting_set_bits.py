"""
Counting Set Bits

Description:
Counting set bits involves determining the number of bits set to '1' in the binary representation of an integer.

Logic:
- Iterate through each bit of the number and count the number of times the least significant bit is 1.
- Right shift the number after each check until the number becomes zero.

Alternatively, use Brian Kernighan’s algorithm which flips the least significant set bit to zero in each iteration.

Time Complexity:
- O(k), where k is the number of set bits

Space Complexity:
- O(1)
"""

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>=1
    return count

def count_set_bits_bk(n):
    count = 0
    while n:
        n &= (n -1)
        count +=1
    return count

def main():
    number = 29  # 11101
    print(f"Number of set bits in {number} is {count_set_bits(number)}")
    print(f"Number of set bits in {number} using Brian Kernighan’s algorithm is {count_set_bits_bk(number)}")

if __name__ == "__main__":
    main()
