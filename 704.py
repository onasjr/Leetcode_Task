## 二分查找
## 二分法
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return []
        if nums[0] == target:
            return 0
        elif nums[-1] == target:
            return len(nums)-1
        left = 0
        right = len(nums)-1
        while left+1 < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1
