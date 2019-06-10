## 只出现一次的数字
## 从第一个数开始异或，直到最后一个，相同项异或为0，不同项和0异或为本身

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in nums[1:]:
            nums[0] ^= i
        return nums[0]
