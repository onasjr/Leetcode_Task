## 摆动排序二
## 从大到小排序，隔一插值

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        nums[::2], nums[1::2] = nums[len(nums)//2:], nums[:len(nums)//2]
        return nums
