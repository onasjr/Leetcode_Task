## 3的幂 超时
## 循环

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n >= 3:
            if n % 3 == 0 and n > 3:
                n = n/3
            if n == 3:
                break
        if n == 3:return True
        else:return False
