## 移动零
## 查找0，记录个数，append

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tmp = 0
        i = 0
        while 0 in nums:
            nums.remove(0)
            i += 1
        while i != 0:
            nums.append(0)
            i -= 1
        return nums
