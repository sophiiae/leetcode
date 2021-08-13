def quickSort(N: list):
	quickSortHelper(N, 0, len(N) - 1)

def quickSortHelper(N, l, r):
	if l < r:
		pivot = partition(N, l, r)
		quickSortHelper(N, l, pivot - 1)
		quickSortHelper(N, pivot + 1, r)

def partition(N, l, r):
	pivot = l
	pivot_value = N[pivot]
	store = l + 1
	for i in range(l + 1, r + 1):
		if N[i] <= pivot_value:
			N[store], N[i] = N[i], N[store]
			store += 1
	N[pivot], N[store - 1] = N[store - 1], N[pivot]
	return store - 1
	
l = [3, 52, 45, 6, 60, 12, 40, 30, 33, 2, 46, 4, 15, 42, 35, 1]

quickSort(l)
print(l)
