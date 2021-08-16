def mergeSort(N: list):
	if len(N) > 1:
		m = len(N) // 2
		L = N[: m]
		R = N[m:]
		mergeSort(L)
		mergeSort(R)
		l = r = i = 0
		while l < len(L) and r < len(R):
			if L[l] < R[r]:
				N[i] = L[l]
				l += 1
			else:
				N[i] = R[r]
				r += 1
			i += 1
		while l < len(L):
			N[i] = L[l]
			l += 1
			i += 1
		while r < len(R):
			N[i] = R[r]
			r += 1
			i += 1

l = [3, 52, 45, 6, 60, 12, 40, 30, 33, 2, 46, 4, 15, 42, 35, 1]
print(l)
mergeSort(l)
print(l)