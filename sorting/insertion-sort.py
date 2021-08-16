def insertionSort(N):
	for i in range(len(N)):
		v = N[i]
		j = i
		while j > 0 and N[j - 1] > N[j]:
			N[j], N[j - 1] = N[j - 1], N[j]
			j -= 1

l = [3, 52, 45, 6, 60, 12, 40, 30, 33, 2, 46, 4, 15, 42, 35, 1]
insertionSort(l)
print(l)
