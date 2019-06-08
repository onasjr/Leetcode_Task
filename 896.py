## 单调数列
## 排序后比较


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        tmp = sorted(A)
        # pdb.set_trace()
        if tmp == A or tmp[::-1] == A:
            return True
        else:
            return False
