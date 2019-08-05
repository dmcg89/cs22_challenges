import functools

def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func

@memoize
def knapsack_recursive(C, items, n):
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
        print('here')
        print(items[n-1][1])
        return knapsack_recursive(C, items, n-1)

    else:
        print('here2')
        return max(items[n-1][2] + knapsack_recursive(C - items[n-1][1], items, n-1), knapsack_recursive(C, items, n-1))

def knapsack_dp(C, items, n):
    K = [[0 for x in range(C+1)] for x in range(n+1)] 
    for i in range(n+1): 
        for w in range(C + 1): 
            if i ==  0 or w == 0: 
                K[i][w] = 0
            # weight < capacity
            elif items[i - 1][1] <= w: 
                #               value           # look of row, items weight , not using current item
                K[i][w] = max(items[i - 1][2] + K[i - 1][w - items[i - 1][1]],  K[i-1][w]) 
            else:
                # weight > capacity
                K[i][w] = K[i-1][w]
    return K[n][C]
    # return K[n]

C = 50
items = (("boot", 10, 60),
        ("tent", 20, 100),
        ("water", 30, 120),
        ("first aid", 15, 70),
        ('thing', 14, 30),
        ('otherthing', 8, 22),
        ('onemorething', 20, 99),
        ('morethings', 30, 30))

print(knapsack_recursive(C, items, len(items)))
# print(knapsack_dp(C, items, len(items)))