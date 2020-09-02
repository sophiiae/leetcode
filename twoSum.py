class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, v in enumerate(nums):
            remain = target - v
            if (remain in table):
                return [table[remain], i]
            table[v] = i