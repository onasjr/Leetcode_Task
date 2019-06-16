## 01矩阵

## 周围补正无穷，比较每个数字周围的数字是否存在0，更新
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])

        res = [[float("inf")] * (col + 2)]
        for i in range(row):
            res.append([float("inf")]+matrix[i]+[float("inf")])
        res.append([float("inf")] * (col + 2))
        # pdb.set_trace()

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if res[i][j] == 1:
                    res[i][j] = min(res[i][j - 1], res[i - 1][j]) + 1

        # pdb.set_trace()
        for i in range(row, 0, -1):
            for j in range(col, 0, -1):
                if res[i][j] != 0:
                    res[i][j] = min(res[i][j + 1]+1, res[i + 1][j]+1, res[i][j])

        ans = []
        for i in range(1, row+1):
            ans.append(res[i][1:col+1])
        return ans
        
