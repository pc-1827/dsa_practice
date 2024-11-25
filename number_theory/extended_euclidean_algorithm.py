"""
Extended Euclidean Algorithm

Description:
The Extended Euclidean Algorithm extends the Euclidean Algorithm to find integers `x` and `y` such that `ax + by = gcd(a, b)`. This is useful in solving Diophantine equations and finding modular inverses.

Logic:
- Recursively apply the Euclidean Algorithm while keeping track of the coefficients.
- Base Case: If `a` is 0, then `gcd(b, 0) = b` and the coefficients are `(0, 1)`.
- Otherwise, recursively compute `gcd(b % a, a)` and update the coefficients.

Time Complexity:
- O(log min(a, b)))

Space Complexity:
- O(1)
"""

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def main():
    a = 30
    b = 20
    gcd_val, x, y = extended_gcd(a, b)
    print(f"GCD of {a} and {b} is {gcd_val}.")
    print(f"Coefficients x and y are {x} and {y} respectively.")
    print(f"Verification: {a}*{x} + {b}*{y} = {a*x + b*y}")

if __name__ == "__main__":
    main()
