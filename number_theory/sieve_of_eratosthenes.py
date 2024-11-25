"""
Sieve of Eratosthenes

Description:
The Sieve of Eratosthenes is an efficient algorithm to find all prime numbers up to a specified integer. It works by iteratively marking the multiples of each prime number starting from 2.

Logic:
- Create a boolean array `is_prime` of size `n+1` and initialize all entries as True. A value in `is_prime[i]` will finally be False if `i` is Not a prime, else True.
- Starting from the first prime number, 2, mark all of its multiples as False.
- Move to the next number in the array and repeat the process until you've processed each number up to the square root of `n`.
- The numbers which remain True in the `is_prime` array are prime numbers.

Time Complexity:
- O(n log log n)

Space Complexity:
- O(n)
"""

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for current in range(2, int(n**0.5) + 1):
        if is_prime[current]:
            for multiple in range(current*current, n + 1, current):
                is_prime[multiple] = False
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def main():
    n = 50
    primes = sieve_of_eratosthenes(n)
    print(f"Prime numbers up to {n}:")
    print(primes)

if __name__ == "__main__":
    main()
