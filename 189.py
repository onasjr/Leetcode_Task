## 旋转数组
## 计算旋转位数，取余；取数组后k位拼接在数组前k

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tmp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = tmp
        return nums
