## 超级次方
## 将b转化为int，调用pow()
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mi = 0
        for i in b:
            mi = mi * 10 + i
        return pow(a, mi, 1337)
