## 爬楼梯：
## 思路1： 递归——到第i阶的方法为从第i-1阶一步和i-2阶两步组成，因此递归计算到第i-1和i-2阶的可能性（超时）
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        else:
            return n
            
## 思路2： 斐波那契数列
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        elif n == 2: return 2
        else:
            a = 1
            b = 2
            for i in range(n-2):
                a, b = b, a+b
            return b
