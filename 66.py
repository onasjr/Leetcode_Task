## 加一
## 将list转换为int，加一后再转换为list

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num + digits[len(digits) - i -1] * (10 ** i)
        num = num + 1
        for i in range(len(str(num))):
            digits[i] = int(str(num)[i])
        return digits



nums = [1,2,3]
ans = Solution().plusOne(nums)
print(ans)
