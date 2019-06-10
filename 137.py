## 只出现一次的数字二
## 使用额外空间，复杂度较高的做法（不太理解解答中三位归0做法）

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = list(set(nums))
        for i in a:
            if nums.count(i) == 1:
                return i
