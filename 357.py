## 计算各个位数不同的数字个数
## 排列组合
n = 1: 10
n = 2: 9*9+10 = 91
n = 3: 9*9*8 + 91

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        res = 10
        tmp = 9
        for i in range(1, n):
            tmp *= 10-i
            res += tmp
        return res
