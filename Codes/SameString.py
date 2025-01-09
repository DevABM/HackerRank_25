# Let's implement the function sameSubstring to find the maximum length of a substring that can be changed with a total cost less than or equal to k. Here’s how you can proceed:

# Calculate the cost to change each character from s[i] to t[i].
# Use a sliding window approach to find the maximum length of a substring where the total cost is within k.

def sameSubstring(s, t, k):
    n = len(s)
    max_length = 0
    current_cost = 0
    start = 0

    for end in range(n):
        current_cost += abs(ord(s[end]) - ord(t[end]))
        
        while current_cost > k:
            current_cost -= abs(ord(s[start]) - ord(t[start]))
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length
