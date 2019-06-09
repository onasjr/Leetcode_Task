## 矩阵置零
## 第一次查找为0位，记为flag
## 之后根据为0位设置行列为0

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        flag = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    flag.append([i,j])
        for i in range(len(flag)):
            # 设置该行为0
            for k in range(col):
                matrix[flag[i][0]][k] = 0
            for k in range(row):
                matrix[k][flag[i][1]] = 0
        return matrix
