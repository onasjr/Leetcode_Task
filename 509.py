## 斐波那契数
## 动态规划

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0]*(N+1)
        if N < 2:
            return N

        dp[0], dp[1] = 0, 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]
