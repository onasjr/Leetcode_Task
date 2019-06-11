## 只出现一次的数字 III
## 将第一遍出现的数字去除，之后再查找一遍该数字，若不存在则为只出现一次的数字

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        initial = list(set(nums))
        res = []
        for i in initial:
            if i in nums:
                nums.remove(i)
            if i not in nums:
                res.append(i)
        return res
