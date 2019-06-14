## 岛屿的周长
## 先对数组补0，之后计算1的个数*4，计算每个1周围1的个数做差

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        ans = 0
        gridnew = [[0]*(col+2)]
        for i in range(row):
            gridnew.append(([0]+grid[i]+[0]))
        gridnew.append(([0]*(col+2)))
        for i in range(1,row+2):
            for j in range(1,col+2):
                if gridnew[i][j] == 1:
                    tmp = sum((gridnew[i-1][j], gridnew[i+1][j], gridnew[i][j-1], gridnew[i][j+1]))
                    ans += 4 - tmp
        return ans
