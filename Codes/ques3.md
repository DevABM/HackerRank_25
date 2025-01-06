Active traders. An institutional broker wants to review their book of customers to see which are most active. Given a list of trades by customer name, determine which customers account for at least 5% of the total number of trades. Order the list alphabetically ascending by name. Example, n equals to 23.

Explanation of Code:
Count Total Trades:

len(customers) gives the total number of trades.
Calculate Threshold:

Multiply total trades by 0.05 to find the minimum number of trades needed for a customer to be considered active.
Count Customer Trades:

Use collections.Counter to count occurrences of each customer in the customers list.
Filter Active Customers:

Include only those customers whose trade count is greater than or equal to the threshold.
Sort Alphabetically:

Use the sort method to arrange the names alphabetically.
Example Walkthrough:
Input:
n = 23
customers = ["BigCar", "SmallCar", "BigCar", "FastCar", ..., "SmallCar"]
Process:
Total trades: 23
Threshold: `23 * 0.05 =