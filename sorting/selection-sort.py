def selectionSort(A: list):
	for i in range(len(A)):
		smallest = i
		for j in range(i+1, len(A)):
			if A[j] < A[smallest]:
				smallest = j
		A[i], A[smallest] = A[smallest], A[i]

test1 = [3,4,6,1,2,8,5,9,0]
selectionSort(test1)

print('test 1:', test1)

test2 = [3,4,6,1,2,8,5,9,0,3,5,1]
selectionSort(test2)

print('test 2:', test2)
