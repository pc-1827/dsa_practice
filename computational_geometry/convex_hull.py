"""
Convex Hull

Description:
The Convex Hull of a set of points is the smallest convex polygon that encloses all the points. One of the common algorithms to find the convex hull is Graham's Scan.

Logic:
- Find the point with the lowest y-coordinate (and leftmost if tie).
- Sort the points based on the polar angle with the reference point.
- Traverse the sorted points and use a stack to maintain the convex hull vertices, ensuring that each turn is counter-clockwise.

Time Complexity:
- O(n log n) due to the sorting step

Space Complexity:
- O(n)
"""

def orientation(p, q, r):
    """Return positive for counter-clockwise, negative for clockwise, zero if colinear."""
    return (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1])

def convex_hull(points):
    # Sort the points lexicographically (first by x, then by y)
    points = sorted(points)

    # Build the lower and upper parts of the hull
    lower = []
    for p in points:
        while len(lower) >=2 and orientation(lower[-2], lower[-1], p) <=0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >=2 and orientation(upper[-2], upper[-1], p) <=0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper to get full hull
    # Remove the last point of each list because it's duplicated
    full_hull = lower[:-1] + upper[:-1]
    return full_hull

def main():
    points = [
        (0, 3),
        (2, 2),
        (1, 1),
        (2, 1),
        (3, 0),
        (0, 0),
        (3, 3)
    ]
    hull = convex_hull(points)
    print("Convex Hull:")
    for point in hull:
        print(point)

if __name__ == "__main__":
    main()
