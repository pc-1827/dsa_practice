"""
Chinese Remainder Theorem

Description:
The Chinese Remainder Theorem provides a solution to a system of simultaneous congruences with pairwise coprime moduli. It finds a unique solution modulo the product of the moduli.

Logic:
- Given a list of remainders and their corresponding pairwise coprime moduli:
    - Compute the product `M` of all moduli.
    - For each modulus `m_i` and remainder `a_i`:
        - Compute `M_i = M / m_i`.
        - Find the modular inverse `y_i` of `M_i` modulo `m_i`.
        - Add to the result: `a_i * y_i * M_i`.
- The final result is the sum of these terms modulo `M`.

Time Complexity:
- O(n^2) due to the computation of modular inverses

Space Complexity:
- O(n)
"""

def extended_gcd(a, b):
    if a ==0:
        return b, 0,1
    gcd_val, x1, y1 = extended_gcd(b %a, a)
    x = y1 - (b//a)*x1
    y = x1
    return gcd_val, x, y

def mod_inverse(a, m):
    gcd_val, x, y = extended_gcd(a, m)
    if gcd_val !=1:
        return None  # Inverse doesn't exist
    else:
        return x % m

def chinese_remainder_theorem(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m
    result =0
    for a_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        y_i = mod_inverse(M_i, m_i)
        if y_i is None:
            return None
        result += a_i * y_i * M_i
    return result % M

def main():
    remainders = [2, 3, 2]
    moduli = [3, 5, 7]
    solution = chinese_remainder_theorem(remainders, moduli)
    if solution is not None:
        print(f"The solution is {solution}, which satisfies:")
        for a, m in zip(remainders, moduli):
            print(f"x ≡ {a} (mod {m})")
    else:
        print("No solution exists for the given system of congruences.")

if __name__ == "__main__":
    main()
