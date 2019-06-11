## 最大正方形
## dp：dp[][]存放以该点为右下角的最大正方形边长，先初始化dp；
## 之后由左边，上边，左上三个点决定是否扩大正方形

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0]*col for i in range(row)]      # 代表以ij为右下角的最大正方形
        maxS = 0

        ## 填充dp初始状态
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    maxS = 1
                else:
                    dp[i][j] = 0

        ## 递归
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == "1":
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    maxS = max(maxS, dp[i][j])
        return maxS*maxS
