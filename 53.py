## 最大自序和
## 动态规划：计算前i项和，与0比较，若小于0，则从第i项开始重新计算自序，否则继续

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1], 0) + nums[i]
        return max(nums)
