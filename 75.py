## 颜色排序
## 思路： 将数据分为0,1,2,；两个指针index1和2表示数组首尾，0放首，2放尾

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        index1 = 0
        index2 = len(nums) - 1
        while i < len(nums):
            if i > index2:
                break
            elif nums[i] == 0:
                nums[i], nums[index1] = nums[index1], nums[i]
                index1 += 1
            elif nums[i] == 2:
                nums[i], nums[index2] = nums[index2], nums[i]
                index2 -= 1
                i -= 1
            i += 1
        return nums
