# input: an array A[1...n] of arbitrary real number (positive, zero, negative).
# output: a contiguous sub-array, say A[i+1...j], of A[1...n] with max element sum (i.e., A[i+1], A[i+2]+...+A[j] is max possible)

def max_sum_subarray(A: []):
	i, j, k = 0, 0, 0
	bestSum, suffixSum = 0, 0
	for t in range(0, len(A)):
		if (suffixSum + A[t] > 0):
			suffixSum += A[t]
		else: 
			suffixSum = 0
			k = t
		if (suffixSum > bestSum):
			bestSum = suffixSum
			i, j = k, t
	return A[i+1: j+1]

print(max_sum_subarray([2, 1, -6, -3, 2, -4, 6, -2, -1, 1, 3, -4, 7, -5, 2, -3]))