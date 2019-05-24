## 缺失数字
## 直接求和

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(1,len(nums)+1)) - sum(nums)
