## 范围求和二
## 计算a和b的最小值相乘

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m*n
        x = y = float("inf")
        
        for p in ops:
            x = min(x, p[0])
            y = min(y, p[1])
        return x*y
