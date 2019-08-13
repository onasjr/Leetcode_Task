## 重复N此的元素
## .count

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lenA = len(A)
        for i in range(len(A)):
            if A.count(A[i]) >= lenA//2:
                return A[i]
