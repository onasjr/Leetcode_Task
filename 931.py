## 下降路径最小和
# 动态规划dp[i][j]存储自上而下到第i行第j个的最小路径和，注意边界
# 转移方程分三种情况
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row = len(A)
        col = len(A[0])

        dp = [[0 for i in range(col)] for j in range(row)]
        dp[0] = A[0] 
        for i in range(1, row):
            for j in range(col):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + A[i][j]
                elif j == col-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1:j+2]) + A[i][j]

        return min(dp[row-1])
