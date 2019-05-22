##给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
## 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
## 二分法查找位置
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index1 = 0
        index2 = len(nums)
        while index1 < index2:
            mid = index1 + (index2 - index1)//2
            if nums[mid] > target:
                index2 = mid
            elif nums[mid] < target:
                index1 = mid + 1
            else:
                return mid
        return index1
