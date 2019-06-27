## 最小差值二
"""
1. 对A排序，从小到大
2. 对于排序后的数组A， 寻找一个节点K的位置，在K之前全部+K， 之后全部-K，计算最大值最小值之间的最小差值(2,lll-1)
3. 当截断点前仅有1个数或最后只有一个数，为特殊情况，分别讨论res最小值
4. 初始化最小值res为A的差值，即考虑到全部加或全部减的情况
"""

class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        res = A[-1] - A[0]
        lll = len(A)
        # 若长度为1
        if lll == 1:
            return 0

        # 对于排序后的数组A， 寻找一个节点K的位置，在K之前全部+K， 之后全部-K
        for i in range(2, lll-1):
            # 最小值
            minnum = min(A[0] + K, A[i] - K)
            # 最大值
            maxnum = max(A[lll - 1] - K, A[i - 1]+K)
            res = min(res, maxnum - minnum)
        i = 1
        if A[0]+K < A[i]-K:
            res = min(res, (A[lll-1]-K)-(A[0]+K))
        else:
            res = min(res, max(A[0]+K, A[lll-1]-K)-(A[i]-K))
        i = lll-1

        if A[i]-K< A[0]+K:
            res = min(res, A[i-1]+K-(A[i]-K))
        else:
            res = min(max(A[i]-K, A[i-1]+K)-(A[0]+K), res)
        return res
