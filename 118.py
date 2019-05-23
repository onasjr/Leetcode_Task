## 杨辉三角
## 第i行中间位置为第i-1行对应位相加

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [1]
        elif numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for n in range(2, numRows):
            res = [1]
            for i in range(len(ans[n-1])):
                if i == len(ans[n-1])-1:
                    res.append(1)
                else:
                    res.append(ans[n-1][i] + ans[n-1][i+1])
                    i += 1
            ans.append(res)
        return ans
