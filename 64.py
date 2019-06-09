## 最小路径和
## 动态规划
## 分为0行，0列，行列不为0三种情况

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(grid[0])]*len(grid)
        m = len(grid)
        n = len(grid[0])
        i, j = 0, 0
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        pdb.set_trace()
        return dp[-1][-1]
