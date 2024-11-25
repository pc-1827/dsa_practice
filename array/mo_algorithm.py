"""
Mo's Algorithm

Description:
Mo's Algorithm is used to answer multiple range queries on an array efficiently. It is particularly useful for queries that require information over subarrays, such as frequency counts or range sums.

Logic:
- Sort the queries in a specific order to minimize the movement of the pointers.
- Initialize the current range to [0, -1] and answer each query by expanding or shrinking the current range.
- Maintain the required information (e.g., frequency counts) as the range changes.

Note:
Implementing Mo's Algorithm from scratch is complex and is generally used for offline queries.

Time Complexity:
- O((n + q) * sqrt(n)) where q is the number of queries

Space Complexity:
- O(n)

"""

def mos_algorithm(arr, queries):
    import math
    block_size = int(math.sqrt(len(arr)))
    queries = sorted(queries, key=lambda x: (x[0]//block_size, x[1] if (x[0]//block_size) %2 ==0 else -x[1]))
    current_l, current_r, current_ans = 0, -1, 0
    freq = {}
    answers = []

    for l, r in queries:
        while current_l > l:
            current_l -=1
            freq[arr[current_l]] = freq.get(arr[current_l],0)+1
            current_ans += arr[current_l]
        while current_r < r:
            current_r +=1
            freq[arr[current_r]] = freq.get(arr[current_r],0)+1
            current_ans += arr[current_r]
        while current_l < l:
            freq[arr[current_l]] -=1
            current_ans -= arr[current_l]
            current_l +=1
        while current_r > r:
            freq[arr[current_r]] -=1
            current_ans -= arr[current_r]
            current_r -=1
        answers.append(current_ans)
    return answers

def main():
    arr = [1, 2, 3, 4, 5]
    queries = [(1,3), (0,4), (2,2)]
    results = mos_algorithm(arr, queries)
    for q, res in zip(queries, results):
        print(f"Sum of range {q} is {res}")

if __name__ == "__main__":
    main()
