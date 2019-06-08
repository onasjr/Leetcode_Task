## 有序数组的平方
## 直接计算之后排序

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = sorted([i**2 for i in A])
        return res
