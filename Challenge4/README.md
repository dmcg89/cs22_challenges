## Challenge 4
### Part 1 - Knapsack Problem
#### Sample input
py knapsack.py OR py dynamic_program.py
### Identify subproblems
Consider each permutation of possible combinations
### Guess first choice
Consider the first item in array as first choice, and consider having that item vs not having that item
### Recursively define the value of an optimal solution
return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),    knapSack(W, wt, val, n-1))
### Compute the value of an optimal solution (recurse and memoize)
Add memoization to above funciton
### Solve original problem - reconstruct from the sub-problems
The recursive function considers all possible permutations of the items array and returns the combination with the max value given a weight constraint.

### Part 2 - Catalan Numbers
### Identify subproblems
Base case: Catalan(0) = 1<br/>
Catalan(s) = ∑{n=1}^n C_{i}C_{n-1}<br/>
Similar to the recursive solution the the Fibonacci Sequence, the subproblems are simply solving for the terms prior to the nth term that is being solved for.


### Guess first choice
Similarly to the Fibonacci Sequence, the first choice is simply going to be the desired input and the term in the sequence before said input.

### Recursively define the value of an optimal solution
result += catalan_recursive(i) * catalan_recursive(n-i-1) 


### Compute the value of an optimal solution (recurse and memoize)
Add memoization to above recursive function
### Solve original problem - reconstruct from the sub-problems
Building up the subproblems from the base case gives the nth term of the Catalan Numbers.