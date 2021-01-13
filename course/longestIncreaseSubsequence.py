# Find the longest monotonically-increasing subsequence of a given sequence of n numbers

# DP algorithm with O(n^2) time



# Patience sort algorithm with O(n log n) time
# Patience sort is similar to solitare card game, it maintains a list of piles which is displayed in decreasing order, the last element of length k is at least as large as the last element of subsequence of length k - 1. 
def getCeilIndex(nums, P, l, r, value):
	while (r - l > 1):
		m = (r + l) // 2
		if (nums[P[m]] >= value):
			r = m
		else:
			l = m
	return r


def LIS(nums: []):
	size = len(nums)
	if size < 2: #base case
		return nums
	
	# initialize piles
	P = [0] * size
	l = 0
	for i in range(1, size):
		if nums[i] < nums[P[0]]: # new smallest value
			P[0] = i 
		elif nums[i] > nums[P[l]]:
			# extend piles
			P[l+1] = i 
			l += 1
		else:
			# replace an existing pile value using binary search
			k = getCeilIndex(nums, P, 0, l, nums[i])
			P[k] = i
	
	result = []
	for i in range(l+1):
		result.append(nums[P[i]])
	return result

a = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]

print(LIS(a))
	
	