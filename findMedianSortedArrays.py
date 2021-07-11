from typing import List

def findMedianSortedArrays1(nums1: List[int], nums2: List[int]) -> float:
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

def findMedianSortedArrays2(nums1: List[int], nums2: List[int]) -> float:
        small = nums1 if len(nums1) < len(nums2) else nums2
        large = nums2 if len(nums1) < len(nums2) else nums1
        start, end = 0, len(small)
        found = False
        partition_total = (len(nums1) + len(nums2) + 1) // 2
        
        while (not found):
            part_small = (start + end) // 2
            part_large = partition_total - part_small
            
            small_left = small[part_small - 1] if part_small > 0 else float('-inf')
            small_right = small[part_small] if part_small < len(small) else float('inf')
            large_left = large[part_large - 1] if part_large > 0 else float('-inf')
            large_right = large[part_large] if part_large < len(large) else float('inf')
            
            if small_left <= large_right and large_left <= small_right:
                found = True
            elif small_left > large_right:
                end = part_small - 1
            else:
                start = part_small + 1
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (max(small_left, large_left) + min(small_right, large_right)) / 2
        return max(small_left, large_left)

a = [1, 2]
b = [3, 4]
print(findMedianSortedArrays2(a, b))