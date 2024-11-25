"""
Euclidean Algorithm (GCD)

Description:
The Euclidean Algorithm is a method to compute the Greatest Common Divisor (GCD) of two integers. It is based on the principle that the GCD of two numbers also divides their difference.

Logic:
- Given two numbers `a` and `b`, replace `a` with `b` and `b` with `a % b`.
- Repeat the process until `b` becomes zero.
- The GCD is the last non-zero value of `a`.

Time Complexity:
- O(log min(a, b)))

Space Complexity:
- O(1)
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a = 56
    b = 98
    result = gcd(a, b)
    print(f"The GCD of {a} and {b} is {result}.")

if __name__ == "__main__":
    main()
