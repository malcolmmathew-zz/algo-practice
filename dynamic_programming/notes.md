# Dynamic Programming notes

Challenging problems sometimes involves optimization. These algorithms require proof that it will always return the best possible solution. For instance, greedy algorithms work by making the best local decision which does not guarantee the best global solution. However, exhaustive solutions that look at every possibility can guarantee the most optimal choice, at great cost however.

DP uses principles from both of these worlds. We can design algorithms that search all possibilities that also store results to avoid recomputing things. This minimizes the work.

DP is used to implement recursive algorithms by storing partial results. The challenge is to see how the recursive algorithm recomputes the same things over and over again. Once that is figured out, use a lookup of some sort to store the results.

## Caching

We can store results of computations using caching. We can avoid recomputing things by checking for a stored valu before trying to compute it. Caching makes sense when we can afford the cost of storage. For something like calculating fibonacci, we can only store n values, so a linear amount of space stored for an exponential recursive solution is a good tradeoff.

## Fibonacci with DP

We can calculate the nth number of fibonacci by explicitly specifying the order of evalaution of the recurrence relation. (refer to fibonacci, def fib_dynamic()). This removes all recursive calls and evaluates the numbers from smallest to biggest and calculates them seqeuentially. This causes O(n) time and space.

## Binomial Coefficients
