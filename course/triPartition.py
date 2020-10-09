#In-place Tri-Partition

#input: ['b', 'g', 'r', 'g', 'g', 'b', 'r', 'g', 'b', 'r', 'r', 'b']
#output: ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'b', 'b', 'b', 'b']

def tri_partition(A: []):
	r, g, b = 0, 0, len(A) - 1
	# LI: 
	# A[0...r-1] are all reds
	# A[r...g-1] are all green
	# A[b+1...n-1] are all blue
	# 0 <= r <= g <= b+1 <= n
	while (g <= b):
		if (A[g] == 'g'):
			g += 1
		elif (A[g] == 'b'):
			A[g], A[b] = A[b], A[g]
			b -= 1
		else:
			A[g], A[r] = A[r], A[g]
			r += 1
			g += 1

input = ['b', 'g', 'r', 'g', 'g', 'b', 'r', 'g', 'b', 'r', 'r', 'b']

tri_partition(input)

print(input)

