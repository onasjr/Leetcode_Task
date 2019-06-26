## 翻转矩阵后的得分
"""
按行遍历，若首位为0，则翻转该行；
按列遍历，若该列为1的个数 < (m//2 + m%2): 翻转该列
最后输出每一行转化为十进制的和

"""
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n  = len(A), len(A[0])
        for i, row in enumerate(A):
            if row[0] == 0:
                row = [1-i for i in row]
                A[i] = row

        for col in range(1, n):
            if sum([row[col] for row in A]) < (m//2 + m%2):
                for row in A:
                    row[col] = 1-row[col]

        return sum([int("".join([str(col) for col in row]), 2) for row in A])
