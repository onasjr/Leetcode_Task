## 搜索二维矩阵2
## 比较每行最后一个数，若比target小则下一行；大则在该行中倒序查找，直到小于或等于target停止；相等时返回T

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        end = -1
        # pdb.set_trace()
        if not matrix:
            return False
        elif not matrix[0]:
            return False
        for hor in matrix:
            while hor[end] > target and end > -len(hor):
                end -= 1
            if hor[end] == target:
                return True
        return False
