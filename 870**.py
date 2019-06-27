## 优势洗牌
"""
1. 对A和B排序；
2. 建立ans， 遍历A中数字，记录比排序后的B中依次数字大的最小A中数字
3. 对于小于B中依次位数字的a， 加入remain
4. 根据原来顺序重建数列，遍历原B排列，如果存在ans[b]， 则append，否则将remain中第一个数加入
"""

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)
        ans = {b: [] for b in B}
        remain = []

        j = 0
        ## 比b中数字大的a中数字
        for a in sortedA:
            if a > sortedB[j]:
                ans[sortedB[j]].append(a)
                j += 1
            else:
                remain.append(a)

        ## 按照原顺序排列答案
        res = []
        for b in B:
            if ans[b]:
                res.append(ans[b].pop())
            else:
                res.append(remain.pop())
        return res
