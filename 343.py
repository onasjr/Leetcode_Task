## 整数拆分
## 动态规划，dp[i]表示整数i可以被分为的最大乘积，则dp[i] = dp[j]*(i-j)和j*(i-j)的最大值，
## 注意初始化dp为1

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(i-1, 1, -1):
                dp[i] = max(dp[i], dp[j] * (i-j), (i-j) * j)
        return dp[n]
