## 在排序数组中查找元素的第一个和最后一个位置
## 库函数查找第一个，遍历查找第二个

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        left = nums.index(target)
        right = []
        # pdb.set_trace()
        for i in range(len(nums[left+1:])):
            if nums[left+1:][i] == target:
                right.append(i)
            else:break
        if not right:
            return [left, left]
        return [left, max(right)+left+1]
