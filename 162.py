## 寻找峰值
## 寻找第一个小于前一个数的位置

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return nums.index(max(nums))
        i = 0
        while nums[i] < nums[i+1]:
            if i < len(nums) - 2:
                i += 1
            else:
                return nums.index(max(nums))
        return i
