## 只有两个键的键盘
## 找规律：次数 = 将该数字能分解为的质数乘积，求质数和

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## 找规律：次数 = 将该数字能分解为的质数乘积，求质数和
        s = 0   # s为结果和
        for i in range(2, n+1):# 分解因数
            if n == 1:break
            while n % i == 0:
                s += i
                n /= i
        return s
