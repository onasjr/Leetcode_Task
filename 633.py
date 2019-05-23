## 平方数之和
## 找到最接近的开方整数，在0~整数区间内寻找两端值平方和与待测数大小关系，若找不到相等则否

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        index2 = int(c**0.5)
        index1 = 0
        if index2**2 == c:
            return True
        while index1 <= index2:
            if index1**2 + index2**2 == c:
                return True
            elif index1**2 + index2**2 < c:
                index1 += 1
            else:
                index2 -= 1
        return False
