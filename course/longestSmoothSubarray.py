# input: s: array of numbers, delta: integer
# output: return the longest subarray is delta smooth
from collections import deque

def longest_smooth_subarray(s: [], delta: int):
	i, j, k = 0, 0, 0
	minlist, maxlist = deque([]), deque([]) # queues to save index of min and max value
	for t in range(0, len(s)):
		# upgrade min
		while (len(minlist) and s[t] > minlist[0] + delta):
			firstmin_index = minlist.popleft()
			k = 1 + firstmin_index
		while (len(maxlist) and maxlist[0] < k):
			maxlist.popleft() #dump max index

		# upgrade max
		while (len(maxlist) and s[t] < maxlist[0] - delta):
			firstmax_index = maxlist.popleft()
			k = 1 + firstmax_index
		while (len(minlist) and minlist[0] < k):
			minlist.popleft() # dump min index

		# compare with previous min, if less than previous min, then previous is not a min
		# remove previous min. Same for max
		while (len(minlist) and s[t] <= s[minlist[-1]]):
			minlist.pop()
		while (len(maxlist) and s[t] >= s[maxlist[-1]]):
			maxlist.pop()

		minlist.append(t)
		maxlist.append(t)

		if j - i < t - k:
			i, j = k, t
	
	return s[i: j+1]
				
arr = [4, -3, 7, 9, 12, 5, 9, 10, 6, 1, 6]

print(longest_smooth_subarray(arr, 8))
		