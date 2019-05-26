## 子集
## 递归：结果 = 除第i位之外的子集 + 除第i为之外的子集都加上第i位

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def eachTime(nums):
            if not nums:
                return [[]]
            first = [nums[0]]
            nums.pop(0)
            sub = eachTime(nums)
            out = [(first + s) for s in sub] + sub
            return out
        return eachTime(nums)
