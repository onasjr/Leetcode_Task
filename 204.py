## 计算质数
## 先将 2－N 的各数放入表中，然后在 2 的上面画一个圆圈，然后划去 2 的其他倍数；
## 第一个既未画圈又没有被划去的数是 3，将它画圈，再划去 3 的其他倍数；
## 现在既未画圈又没有被划去的第一个数是 5，将它画圈，并划去5的其他倍数……依次类推，一直到所有小于或等于N的各数都画了圈或划去为止。


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        res = [1] * n
        res[0],res[1] = 0, 0
        for i in range(2, int(n**0.5)+1):     # 将删除范围定为2—sqrt(n)之间
            if res[i] == 1:
                res[i*i:n:i] = [0] * len(res[i*i:n:i])
        return sum(res)
