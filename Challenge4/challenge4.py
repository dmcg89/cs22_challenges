def knapsack(C, items, n):
    ''' A  method to determine the maximum value of the items included in the knapsack 
    without exceeding the capacity  C

    Parameters: 
    C= 50
    items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
    Returns: max value
    Credit: Geeks for geeks
'''
    # Base Case
    if n == 0 or C == 0:
        return 0

    # If weight of the nth item is is more than the knapsack capacity,
    # then this item is not included in optimal solution
    if items[n-1][1] > C:
        return knapsack(C, items, n-1)

    else:
        return max(items[n-1][2] + knapsack(C - items[n-1][1], items, n-1), knapsack(C, items, n-1))

C = 50
items = (("boot", 10, 60),
        ("tent", 20, 100),
        ("water", 30, 120),
        ("first aid", 15, 70))

print(knapsack(C, items, len(items)))