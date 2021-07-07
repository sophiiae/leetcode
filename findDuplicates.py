# LeetCode 287
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums (can repeat multiple times), return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicates(nums):
	# Find the intersection point of the two runners.
	tortoise = hare = nums[0]
	print('start: ' + str(tortoise))
	print('phrase 1 =============')
	while True:
		tortoise = nums[tortoise]
		hare = nums[nums[hare]]
		print('tortoise: ' + str(tortoise))
		print('hare: ' + str(hare))
		if tortoise == hare:
			break
	
	# Find the "entrance" to the cycle.
	tortoise = nums[0]
	print('phrase 2 =============')
	while tortoise != hare:
		tortoise = nums[tortoise]
		hare = nums[hare]
		print('tortoise: ' + str(tortoise))
		print('hare: ' + str(hare))
	
	return hare

t1 = [2, 9, 1, 5, 3, 6, 8, 9, 7, 9]
findDuplicates(t1)
