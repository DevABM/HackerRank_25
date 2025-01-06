def maxPresentations(scheduleStart, scheduleEnd):
    # Combine start and end times into a list of tuples
    presentations = list(zip(scheduleStart, scheduleEnd))
    
    # Sort presentations by their end times
    presentations.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = 0
    
    for start, end in presentations:
        if start >= last_end_time:
            # Attend this presentation
            count += 1
            last_end_time = end
    
    return count

# Example usage
scheduleStart = [1, 2, 4, 6, 8]
scheduleEnd = [3, 5, 7, 8, 9]
result = maxPresentations(scheduleStart, scheduleEnd)
print(result)  # Output: 3
