## Pow(x,n)
## 递归，利用指数是否是2的倍数减少迭代次数

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)
