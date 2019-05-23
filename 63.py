## 不同路径②
## 动态规划
## 将第一行第一列记为1，其中出现障碍位（1）的位之后记为0,0表示不能走该路线
## 则右下角位置的可能路线为左边和上边路线和：obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]

        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
        return obstacleGrid[m-1][n-1]
