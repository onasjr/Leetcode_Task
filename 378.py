## 有序矩阵中第k小的元素
## 转化为一维，sort

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        for i in range(len(matrix)):
            nums.extend(matrix[i])
        return sorted(nums)[k-1]
