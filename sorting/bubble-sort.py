def bubbleSortAsce(A: list):
	for i in reversed(range(len(A))):
		for j in range(i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]

test1 = [3,4,6,1,2,8,5,9,0]
bubbleSortAsce(test1)

print('test 1:', test1)

test2 = [3,4,6,1,2,8,5,9,0,3,5,1]
bubbleSortAsce(test2)

print('test 2:', test2)

def bubbleSortDesc(N: list):
	for i in range(len(N)):
		for j in range(len(N)-i-1):
			if N[j] > N[j+1]:
				N[j], N[j+1] = N[j+1], N[j]


l = [3, 52, 45, 6, 60, 12, 40, 30, 33, 2, 46, 4, 15, 42, 35, 1]
bubbleSortDesc(l)
print(l)

