Here’s a Python function named maxPresentations that takes two lists, scheduleStart and scheduleEnd, representing the start and end times of presentations respectively. It computes the maximum number of non-overlapping presentations you can attend:
Explanation:
Combine Start and End Times: Use zip to pair the start and end times into tuples for easier sorting and iteration.
Sort by End Times: Sort the presentations based on their end times to ensure we always consider the earliest finishing presentation.
Iterate and Select Presentations: Use a greedy approach:
Attend the presentation if its start time is greater than or equal to the end time of the last attended presentation.
Count Non-Overlapping Presentations: Increment the count for each non-overlapping presentation.
This ensures the maximum number of presentations that can be attended without conflicts.