"""
Activity Selection Problem

Description:
The Activity Selection Problem is a classic example of a greedy algorithm. The goal is to select the maximum number of activities that don't overlap, given their start and finish times.

Logic:
- Sort the activities based on their finish times.
- Initialize the first activity as selected.
- Iterate through the sorted activities and select the next activity that starts after the current activity finishes.
- Continue this process to maximize the number of non-overlapping activities.

Time Complexity:
- O(n log n) due to the sorting step

Space Complexity:
- O(n) for storing the sorted activities
"""

def activity_selection(activities):
    # Sort activities based on finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    selected = []

    # The first activity always gets selected
    last_finish_time = sorted_activities[0][1]
    selected.append(sorted_activities[0])

    # Iterate through the sorted activities
    for activity in sorted_activities[1:]:
        if activity[0] >= last_finish_time:
            selected.append(activity)
            last_finish_time = activity[1]

    return selected

def main():
    activities = [
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (3, 9),
        (5, 9),
        (6, 10),
        (8, 11),
        (8, 12),
        (2, 13),
        (12, 14)
    ]
    selected_activities = activity_selection(activities)
    print("Selected activities:")
    for activity in selected_activities:
        print(f"Start: {activity[0]}, Finish: {activity[1]}")

if __name__ == "__main__":
    main()
