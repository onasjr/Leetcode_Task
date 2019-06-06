## 数组中重复的数据
## 排序，寻找相邻相等元素

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = 0
        tmp = []
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                tmp.append(nums[i])
                i += 2
            else:
                i += 1
        return tmp
