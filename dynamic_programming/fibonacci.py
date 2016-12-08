def fib_recursive(n):
	if n==0:
		return 0
	if n==1:
		return 1

	return fib_recursive(n-2) + fib_recursive(n-1)



print fib_recursive(3)
