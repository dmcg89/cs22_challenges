# Find nth term in catalan number sequence
# credit: geeksforgeeks.com

# ---------------------------------------------
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


# A recursive function to find nth catalan number
@memoize
def catalan_recursive(n): 
    # Base Case 
    if n <=1 : 
        return 1 
  
    # Catalan(n) is the sum of catalan(i)*catalan(n-i-1) 
    res = 0 
    for i in range(n): 
        res += catalan_recursive(i) * catalan_recursive(n-i-1) 
  
    return res 

# A dynamic programming based function to find nth 
# Catalan number 
def catalan_iterative(n): 
    if (n == 0 or n == 1): 
        return 1
  
    # Table to store results of subproblems 
    catalan = [0 for i in range(n + 1)] 
  
    # Initialize first two values in table 
    catalan[0] = 1
    catalan[1] = 1
  
    # Fill entries in catalan[] using recursive formula 
    for i in range(2, n + 1): 
        catalan[i] = 0
        for j in range(i): 
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1] 
  
    # Return last entry 
    return catalan[n] 

# Driver Program to test above function 
for i in range(30): 
    # print(catalan_recursive(i))
    print(catalan_iterative(i))


