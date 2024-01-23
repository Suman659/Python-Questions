#Implementation of Toy Problem

def minCost(ratings, n):
    res = 0
    
    # fill 1 in both array
    left2right = [1 for i in range(n)]
    right2left = [1 for i in range(n)]

    # Traverse from left to right and assign
    # minimum possible rating considering only
    # left adjacent
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left2right[i] = left2right[i - 1] + 1

    # Traverse from right to left and assign
    # minimum possible rating considering only
    # right adjacent
    i = n - 2
    while i >= 0:
        if ratings[i] > ratings[i + 1]:
            right2left[i] = right2left[i + 1] + 1
        i -= 1
    
    # Calculate cost based on the longer sequence at each position
    for i in range(n):
        res += max(left2right[i], right2left[i]) * ratings[i]
    
    return res

# Example usage:
ratings = [1, 6, 8, 3, 4, 1, 5, 7]
n = len(ratings)
total_cost = minCost(ratings, n)

print("Total cost to buy all books:", total_cost)
