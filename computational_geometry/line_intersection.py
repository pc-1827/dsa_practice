"""
Line Intersection

Description:
Determining if two line segments intersect and finding the point of intersection if they do.

Logic:
- Use the orientation method to check the general and special cases of intersection.
- If the orientations satisfy the intersection conditions, calculate the intersection point using line equations.

Time Complexity:
- O(1)

Space Complexity:
- O(1)
"""

def on_segment(p, q, r):
    """Check if point q lies on segment pr"""
    if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
        return True
    return False

def orientation(p, q, r):
    """Find the orientation of ordered triplet (p, q, r)."""
    val = (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1])
    if val ==0:
        return 0  # colinear
    return 1 if val >0 else 2  # clock or counterclock wise

def do_intersect(p1, q1, p2, q2):
    """Check if line segments p1q1 and p2q2 intersect."""
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    if o1 ==0 and on_segment(p1, p2, q1):
        return True
    if o2 ==0 and on_segment(p1, q2, q1):
        return True
    if o3 ==0 and on_segment(p2, p1, q2):
        return True
    if o4 ==0 and on_segment(p2, q1, q2):
        return True
    return False

def compute_intersection(p1, q1, p2, q2):
    """Compute the intersection point of lines p1q1 and p2q2 if they intersect."""
    A1 = q1[1] - p1[1]
    B1 = p1[0] - q1[0]
    C1 = A1*p1[0] + B1*p1[1]

    A2 = q2[1] - p2[1]
    B2 = p2[0] - q2[0]
    C2 = A2*p2[0] + B2*p2[1]

    determinant = A1*B2 - A2*B1
    if determinant ==0:
        return None  # Lines are parallel or colinear
    else:
        x = (B2*C1 - B1*C2) / determinant
        y = (A1*C2 - A2*C1) / determinant
        return (x, y)

def main():
    # Example 1: Intersecting lines
    p1 = (1, 1)
    q1 = (4, 4)
    p2 = (1, 8)
    q2 = (2, 4)
    if do_intersect(p1, q1, p2, q2):
        intersection = compute_intersection(p1, q1, p2, q2)
        print(f"Lines intersect at {intersection}")
    else:
        print("Lines do not intersect.")

    # Example 2: Non-intersecting lines
    p3 = (1, 1)
    q3 = (2, 2)
    p4 = (3, 3)
    q4 = (4, 4)
    if do_intersect(p3, q3, p4, q4):
        intersection = compute_intersection(p3, q3, p4, q4)
        print(f"Lines intersect at {intersection}")
    else:
        print("Lines do not intersect.")

if __name__ == "__main__":
    main()
