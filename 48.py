## 旋转图像（运行结果不同）
## 找规律：先上下翻转，再交换主对角线两边数字

## 翻转整个数组,再按正对角线交换两边的数
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix = matrix[::-1]
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
