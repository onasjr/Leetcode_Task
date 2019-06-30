## 最低票价
# 动态规划，dp[i]为截至到days[i]天所需要的最小花费，双指针i为当前截至到的天数，j为向前遍历寻找最小值的指针
# 如下

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        n = len(days)
        dp = [float("inf") for i in range(n)]
        dp[0] = min(costs)
        
        for i in range(1, n):
            # 无论如何，初始截止到第i天的所需花费为前一天花费+一天票价
            dp[i] = dp[i - 1] + min(costs)
            # 由第i天向前遍历
            for j in range(i - 1, -1, -1):
                if days[i] - days[j] < 7:
                    # 差值在7以内，则总花费最小值 = min(第j-1天花费加第j天买7天票，第i天买一天票)
                    dp[i] = min(dp[i], (dp[j - 1] if j >= 1 else 0) + costs[1])
                if days[i] - days[j] < 30:
                    # 差值在30以内，则总花费最小值 = min(第j-1天花费加第j天买30天票，第i天买一天票)                    
                    dp[i] = min(dp[i], (dp[j - 1] if j >= 1 else 0) + costs[2])
        # dp[n-1]为到最后一天所需要的最小花费和
        return dp[n - 1]
