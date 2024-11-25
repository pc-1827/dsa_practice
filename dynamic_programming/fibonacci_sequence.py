"""
Fibonacci Sequence

Description:
The Fibonacci Sequence is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1. It is a classic example of a dynamic programming problem that can be solved efficiently using memoization or tabulation.

Logic:
- Use memoization to store previously computed Fibonacci numbers to avoid redundant calculations.
- Alternatively, use iterative tabulation to build up the sequence from the bottom up.

Time Complexity:
- O(n)

Space Complexity:
- O(n) for memoization or O(1) for iterative approach
"""

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def main():
    n = 10
    print(f"Fibonacci number at position {n} (memoization): {fibonacci_memo(n)}")
    print(f"Fibonacci number at position {n} (iterative): {fibonacci_iterative(n)}")

if __name__ == "__main__":
    main()
