"""
Closest Pair of Points

Description:
Finding the closest pair of points in a set involves determining the two points with the minimum distance between them. A divide and conquer approach can solve this problem efficiently.

Logic:
- Sort the points based on their x-coordinates.
- Recursively divide the set of points into two halves.
- Find the smallest distance in each half.
- Check pairs of points across the dividing line that are within the minimum distance found.
- Return the overall minimum distance and the pair of points.

Time Complexity:
- O(n log n) due to the sorting and divide and conquer approach

Space Complexity:
- O(n) for storing the points and auxiliary data structures
"""

import math

def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair

def strip_closest(strip, d):
    """Find the closest pair in the strip where points are sorted by y-coordinate."""
    min_dist = d
    pair = (None, None)
    strip = sorted(strip, key=lambda x: x[1])
    for i in range(len(strip)):
        j = i +1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                pair = (strip[i], strip[j])
            j +=1
    return min_dist, pair

def closest_pair_recursive(points_sorted_x):
    n = len(points_sorted_x)
    if n <=3:
        return brute_force(points_sorted_x)

    mid = n //2
    mid_point = points_sorted_x[mid]

    dl, pair_l = closest_pair_recursive(points_sorted_x[:mid])
    dr, pair_r = closest_pair_recursive(points_sorted_x[mid:])

    if dl < dr:
        d = dl
        pair = pair_l
    else:
        d = dr
        pair = pair_r

    # Build strip
    strip = []
    for point in points_sorted_x:
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)

    ds, pair_ds = strip_closest(strip, d)
    if ds < d:
        return ds, pair_ds
    return d, pair

def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda x: x[0])
    return closest_pair_recursive(points_sorted_x)

def main():
    points = [
        (2, 3),
        (12, 30),
        (40, 50),
        (5, 1),
        (12, 10),
        (3, 4)
    ]
    min_dist, pair = closest_pair(points)
    print(f"Closest pair: {pair} with distance {min_dist}")

if __name__ == "__main__":
    main()
