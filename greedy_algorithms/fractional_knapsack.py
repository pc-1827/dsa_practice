"""
Fractional Knapsack Problem

Description:
The Fractional Knapsack Problem is a variation where the thief can take fractions of an item rather than the whole item. The goal is to maximize the total value in the knapsack without exceeding its capacity.

Logic:
- Calculate the value-to-weight ratio for each item.
- Sort the items in decreasing order of their value-to-weight ratio.
- Iterate through the sorted items and add as much of each item to the knapsack as possible.
- If the knapsack can't accommodate the entire item, add the fractional part.

Time Complexity:
- O(n log n) due to sorting

Space Complexity:
- O(n) for storing the sorted items
"""

def fractional_knapsack(capacity, items):
    # items is a list of tuples (value, weight)
    # Calculate value to weight ratio
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if capacity <=0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity =0
    return total_value

def main():
    capacity = 50
    items = [
        (60, 10),
        (100, 20),
        (120, 30)
    ]
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in the knapsack: {max_value}")

if __name__ == "__main__":
        main()
