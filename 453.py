## 最小移动次数使数组元素相等
## 使每个元素减一得到数组最小值所需要的次数即为其他元素加一相同的次数


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = min(nums)
        return sum(i-tmp for i in nums)
