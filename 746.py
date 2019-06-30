## 使用最小花费爬楼梯
# 动态规划，dp[i]为爬到第i级花费的最小能量，转移方程：dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])，
# 最后一级台阶转移方程：        dp[lll-1] = min(dp[lll-3]+cost[lll-1], dp[lll-2])


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        lll = len(cost)
        dp = [0 for i in range(lll)]
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, lll-1):
            # pdb.set_trace()
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])
        dp[lll-1] = min(dp[lll-3]+cost[lll-1], dp[lll-2])
        return dp[-1]
