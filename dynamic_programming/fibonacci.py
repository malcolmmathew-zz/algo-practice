def fib_recursive(n):
	if n==0:
		return 0
	if n==1:
		return 1

	return fib_recursive(n-2) + fib_recursive(n-1)

max_n = 45
unknown = -1
arr = [unknown for unknown in range(max_n)]
arr[0] = 0
arr[1] = 1

def fib_dynamic(n):
	if arr[n] == unknown:
		arr[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
	return arr[n]

print fib_recursive(3)
print fib_dynamic(4)
