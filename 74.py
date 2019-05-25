## 搜索二维矩阵
## 比较每行最后一个

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        elif not matrix[0]:
            return False
        end = -1
        for hor in matrix:
            while hor[end] > target and end > -len(hor):
                end -= 1
            if hor[end] == target:
                return True
        return False
