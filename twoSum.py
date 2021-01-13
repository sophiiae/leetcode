def twoSum1(nums: list, target: int) -> list:
	table = {}
	for i, v in enumerate(nums):
		remain = target - v
		if (remain in table):
			return [table[remain], i]
		table[v] = i

def twoSum2(nums: list, target: int) -> list:
	nums.sort()
	left, right = 1, len(nums) - 1
	while(left < right):
		sum = nums[left] + nums[right]
		if sum == target:
			return [nums[left], nums[right]]
		elif sum > target:
			right -= 1
		else:
			left += 1

l = [1, 6, 5, 7, 12, 4, 2, 9]
target = 9
print(twoSum2(l, target))

