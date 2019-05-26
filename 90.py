## 子集2
## 迭代，同子集题目思路，之后增加排序和去重操作

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def eachTime(nums):
            if not nums:
                return [[]]
            first = [nums[0]]
            nums.pop(0)
            sub = sorted(eachTime(nums))
            out = [sorted(first + s) for s in sub] + sub
            return out
        out = eachTime(nums)
        ans = []
        for i in out:
            if i not in ans:
                ans.append(i)
        return sorted(ans)
