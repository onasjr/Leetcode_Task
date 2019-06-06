## 存在重复元素
## set(nums)，比较长度

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp = set(nums)
        if len(tmp) == len(nums):
            return False
        else:
            return True
