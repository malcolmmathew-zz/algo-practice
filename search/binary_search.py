arr = [1, 3, 7, 32, 60, 70, 80]


def binary_search(val, minim, maxim):
	mid_x = (maxim - minim) / 2 + minim

	if maxim<minim:
		return False

	if val == arr[mid_x]:
		return True

	if val < arr[mid_x]:
		return binary_search(val, minim, mid_x)
	else:
		return binary_search(val, mid_x, maxim)

	
for i in arr:
	print binary_search(i, 0, len(arr))