## 山脉数组的峰顶索引
## 寻找第一个小于前一个数的位置

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        while A[i] < A[i+1]:
            if i < len(A) - 2:
                i += 1
        return i
