def bubbleSort(A: list):
	for i in reversed(range(len(A))):
		for j in range(i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]

test1 = [3,4,6,1,2,8,5,9,0]
bubbleSort(test1)

print('test 1:', test1)

test2 = [3,4,6,1,2,8,5,9,0,3,5,1]
bubbleSort(test2)

print('test 2:', test2)