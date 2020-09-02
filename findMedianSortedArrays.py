from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) > len(nums2)):
            # ensure when partition x gets shortter, partition y has enough elements
            temp = nums1
            nums1 = nums2
            nums2 = temp
        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x
        while(low <= high):
			# use binary search
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            if (maxLeftX <= minRightY and maxLeftY <= minRightX):
                if ((x + y) % 2):
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            elif (maxLeftX > minRightY):
                high = partitionX - 1
            else:
                low = partitionX + 1
