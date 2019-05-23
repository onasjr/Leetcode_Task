## 不同路径
## m*n方格，即为一共需要走m+n-2步，从中挑出n-1步向下走 即为排列组合问题

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = math.factorial(m+n-2)/math.factorial(n-1)/math.factorial(m-1)

        return ans

## 动态规划

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        dp = [[0]*n]*m
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
