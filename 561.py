## 数组拆分 I
## 组合后最小值和即为从小到大排序的奇数位和

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[0::2])
