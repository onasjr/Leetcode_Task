## Gray编码
## 递归调用
## 规律：第i行是第i-1行由左边开始前加0，和由右边的镜像前加1组成

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        def eachTimes(n):
            if n == 1:
                return ["0", "1"]
            tmp = eachTimes(n-1)
            ans = []
            for i in tmp:
                ans.append("0" + i)
            tmp_right = tmp[::-1]
            for j in tmp_right:
                ans.append("1" + j)
            return ans
        res = eachTimes(n)
        ans = [int(i, 2) for i in res]
        return ans
