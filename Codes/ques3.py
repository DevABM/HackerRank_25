from collections import Counter

def getActiveTraders(customers):
    # Step 1: Count total trades
    total_trades = len(customers)
    
    # Step 2: Calculate the 5% threshold
    threshold = total_trades * 0.05
    
    # Step 3: Count trades per customer
    customer_counts = Counter(customers)
    
    # Step 4: Filter customers meeting the threshold
    active_customers = [customer for customer, count in customer_counts.items() if count >= threshold]
    
    # Step 5: Sort the result alphabetically
    active_customers.sort()
    
    return active_customers

# Example usage
n = 23
customers = [
    "BigCar", "SmallCar", "BigCar", "FastCar", "BigCar",
    "SmallCar", "SmallCar", "FastCar", "BigCar", "SmallCar",
    "BigCar", "FastCar", "FastCar", "FastCar", "SmallCar",
    "BigCar", "BigCar", "SmallCar", "FastCar", "BigCar",
    "FastCar", "BigCar", "SmallCar"
]
result = getActiveTraders(customers)
print(result)  # Output: ['BigCar', 'SmallCar']
