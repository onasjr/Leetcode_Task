## 排列硬币
依次减去1,2,3···，减去k次，如果最后n为0，k-1；n为负，k-2


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        times = 1
        while n > 0:
            n -= times
            times += 1
        if n == 0:
            return times-1
        else:
            return times-2
