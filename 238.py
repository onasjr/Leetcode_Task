## 除自身以外数组的乘积
## 开辟一个len（nums）长度空间ans存放乘积，先从左到右依次存放截止到该位之前的乘积，
## 之后从右到左计算截止到该位之后的乘积，并将两者相乘

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0]*n
        tmp = 1
        for i in range(n):
            ans[i] = tmp
            tmp *= nums[i]
        tmp = 1
        i = n-1
        while i >= 0:
            ans[i] *= tmp
            tmp *= nums[i]
            i -= 1
        return ans
