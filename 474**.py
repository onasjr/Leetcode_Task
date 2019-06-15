## 一和零
## dp二维背包问题


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ## [0:i-1]的字符串物品中，j个0，k个1最多能够构成字符串数量。字符串为物品，0,1数量为背包限制。
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for k in strs:
            t = 0
            y = 0
            for j in k:
                if j == "0":
                    y += 1
                else:
                    t += 1
            
            for i in range(n, -1, -1):
                for j in range(m, -1, -1):
                    if i-t >= 0 and j-y >= 0:
                        dp[i][j] = max(dp[i][j], 1+dp[i-t][j-y])
        return dp[-1][-1]
