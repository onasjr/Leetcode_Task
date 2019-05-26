## 三角形最小路径和
## 动态规划，每个位置的值为自底向上到该位置的最小路径和，triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

class Solution:
    def minimumTotal(self, triangle):
        for i in range(len(triangle)-2, -1, -1):        # 从倒数第二行开始，自底向上，计算截止到每个位置的最小值
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])     # 根据题意，只能取下一行该位置或右边位置
        return triangle[0][0]
