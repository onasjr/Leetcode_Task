## 数字范围按位与
## 排除三种特殊情况，其他按位与

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        if m == n:
            return m
        if len(bin(m)) != len((bin(n))):
            return 0
        ff = m
        for i in range(m, n + 1):
            ff &= i
        return ff
