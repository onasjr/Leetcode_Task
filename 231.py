## 2的幂
## 循环比较，依次生成2**i

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = 1
        i = 1
        while tmp <= n:
            if tmp == n:
                return True
            else:
                tmp = 2**i
                i += 1
        return False
