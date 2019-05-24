## 求众数
## 由题目可得，众数的个数>n/2，因此排序后去中间位置即为结果

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        index = length // 2
        nums = sorted(nums)
        return nums[index]
