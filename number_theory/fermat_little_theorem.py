"""
Fermat's Little Theorem

Description:
Fermat's Little Theorem states that if `p` is a prime number, then for any integer `a` such that `a` is not divisible by `p`, `a^(p-1) ≡ 1 (mod p)`. It is widely used in primality testing and cryptography.

Logic:
- Given a prime `p` and an integer `a` not divisible by `p`, compute `a^(p-1) % p`.
- If the result is 1, it satisfies Fermat's Little Theorem.
- This can be used as a primality test, although it has limitations with Carmichael numbers.

Time Complexity:
- O(log p) due to modular exponentiation

Space Complexity:
- O(1)
"""

def fermat_little_theorem(a, p):
    if p <=1:
        return False
    if a % p ==0:
        return False
    return pow(a, p-1, p) ==1

def main():
    a = 2
    p = 7
    if fermat_little_theorem(a, p):
        print(f"{a}^{p-1} ≡ 1 (mod {p}) holds true.")
    else:
        print(f"{a}^{p-1} ≡ 1 (mod {p}) does not hold true.")

if __name__ == "__main__":
    main()
