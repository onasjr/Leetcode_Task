## 搜索旋转排序数组 II
## 直接查找

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return target in nums
