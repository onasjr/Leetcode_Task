## 数组中的K-diff数对
## 寻找+k数字是否存在

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        res = 0
        if k == 0:
            for i in set(nums):
                if nums.count(i) > 1:
                    res += 1
            return res
        nums = list(set(nums))
        for i in nums:
            if i + k in nums:
                res += 1
        return res
