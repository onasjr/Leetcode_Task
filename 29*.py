## 两数相除
## 增倍除数，除数大于被除数时倍减除数，注意2**31特殊情况


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # t:翻倍倍数
        a, b, r, t = abs(dividend), abs(divisor), 0, 1
        while a >= b or t > 1:
            if a >= b:
                r += t
                a -= b
                b += b
                t += t
            else:
                t >>= 1 # a >> b 相当于 a // 2**b
                b >>= 1
        if divisor*dividend < 0:r = -r
        return min(max(-2 ** 31, r), 2 ** 31 - 1)
