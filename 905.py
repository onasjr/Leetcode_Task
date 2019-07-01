## 按奇偶排序数组
# 偶数ans1， 奇数ans2

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans1 = []
        ans2 = []
        for i in A:
            if i % 2 == 0:
                ans1.append(i)
            else:
                ans2.append(i)
        return ans1+ans2
