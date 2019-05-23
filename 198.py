## 打家劫舍
## 计算单数位和双数位数字和，比较


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        import copy
        nums1 = [nums[2*i] for i in range(math.ceil(len(nums)/2))]
        nums2 = [nums[2*i + 1] for i in range(math.floor(len(nums)/2))]
        if sum(nums1) >= sum(nums2):
            return sum(nums1)
        else:
            return sum(nums2)
