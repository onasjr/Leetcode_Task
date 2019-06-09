## 寻找两个有序数组的中位数
## 拼接排序找中位数（时间复杂度不符合要求）

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 0:
            return float((nums[n//2-1] + nums[n//2]) / 2.0)
        else:
            return nums[n//2]
