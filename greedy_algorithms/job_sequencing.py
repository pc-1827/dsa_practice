"""
Job Sequencing Problem

Description:
The Job Sequencing Problem involves scheduling jobs to maximize total profit when each job takes a single unit of time and requires a deadline by which it must be completed.

Logic:
- Sort the jobs in decreasing order of profit.
- Initialize the result sequence and occupied slots.
- Iterate through the sorted jobs and place each job in the latest possible free slot before its deadline.
- If no such slot is available, skip the job.

Time Complexity:
- O(n log n) due to sorting

Space Complexity:
- O(n) for result and occupied slots
"""

def job_sequencing(jobs, max_deadline):
    # jobs is a list of tuples (job_id, deadline, profit)
    # Sort jobs based on profit in descending order
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    result = [None] * max_deadline
    total_profit = 0
    for job in sorted_jobs:
        for slot in range(min(max_deadline, job[1])-1, -1, -1):
            if result[slot] is None:
                result[slot] = job[0]
                total_profit += job[2]
                break
    scheduled_jobs = [job for job in result if job is not None]
    return scheduled_jobs, total_profit

def main():
    jobs = [
        ('a', 2, 100),
        ('b', 1, 19),
        ('c', 2, 27),
        ('d', 1, 25),
        ('e', 3, 15)
    ]
    max_deadline = max(job[1] for job in jobs)
    scheduled_jobs, total_profit = job_sequencing(jobs, max_deadline)
    print(f"Scheduled Jobs: {scheduled_jobs}")
    print(f"Total Profit: {total_profit}")

if __name__ == "__main__":
    main()
