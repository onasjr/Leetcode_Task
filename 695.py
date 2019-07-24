## 岛屿的最大面积
# 思路：遍历grid中为1的数值，地柜调用dfs
# dfs，对当前ij位置扩散搜索，查找过的点设为2，更新area值，最后返回

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            area = 1
            # 查找过的点设为2
            grid[i][j] = 2
            area += dfs(grid, i, j-1)
            area += dfs(grid, i, j+1)
            area += dfs(grid, i-1, j)
            area += dfs(grid, i+1, j)
            return area
            
        res = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(dfs(grid, i, j), res)
        
        return res
