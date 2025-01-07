def getMinCost(crews, repairs):
    # Sort both the crew locations and repair locations
    crews.sort()
    repairs.sort()
    
    # Calculate the total distance by summing up the absolute differences
    total_distance = sum(abs(c - r) for c, r in zip(crews, repairs))
    
    return total_distance

# Example usage:
crews = [1, 3, 5]
repairs = [3, 5, 7]
result = getMinCost(crews, repairs)
print(result)  # Output: 6
