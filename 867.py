## 转置矩阵
## 循环嵌套

class Solution:
    def transpose(self, A):
        result = []
        for i in range(len(A[0])):
            result.append([])
            for j in range(len(A)):
                result[i].append(A[j][i])
        return result
