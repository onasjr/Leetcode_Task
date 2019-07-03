## 图片平滑器
# 在周围padding0，之后分情况讨论，顶点，边缘上点，中间点，注意row/col为1的情况

class Solution:
    def imageSmoother(self, M):
        row = len(M)
        col = len(M[0])
        tmp = []
        tmp.append([0 for _ in range(col+2)])
        for i in range(row):
            tmp.append(([0]+M[i]+[0]))
        tmp += [[0 for _ in range(col+2)]]
        temp = 0
        if row == col == 1:
            return M

        ans = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(1,row+1):
            for j in range(1, col+1):
                temp = sum([tmp[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2)])
                if ((i == 1 or i == row) and (j != 1 and j != col)) or ((i != 1 and i != row) and (j == 1 or j == col)):
                    ans[i-1][j-1] = temp // 6 if row != 1 and col != 1 else temp//3
                elif (i == 1 or i == row) and (j == 1 or j == col):
                    ans[i-1][j-1] = temp // 4 if row != 1 and col != 1 else temp//2
                else:
                    ans[i-1][j-1] = temp//9

        return ans
