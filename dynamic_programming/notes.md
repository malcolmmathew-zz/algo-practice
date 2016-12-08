## Dynamic Programming notes

Challenging problems sometimes involves optimization. These algorithms require proof that it will always return the best possible solution. For instance, greedy algorithms work by making the best local decision which does not guarantee the best global solution. However, exhaustive solutions that look at every possibility can guarantee the most optimal choice, at great cost however. 

DP uses principles from both of these worlds. We can design algorithms that search all possibilities that also store results to avoid recomputing things. This minimizes the work. 

DP is used to implement recursive algorithms by storing partial results. The challenge is to see how the recursive algorithm recomputes the same things over and over again. Once that is figured out, use a lookup of some sort to store the results.
