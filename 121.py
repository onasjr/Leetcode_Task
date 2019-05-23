## 买卖股票的最佳时机
## 动态规划：（超时）
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ans = [0]*len(prices)
        for i in range(len(prices)):
            if i == 0:
                ans[i] = 0
            else:
                ans[i] = max(ans[i-1], prices[i] - min(prices[:i]))
        return max(ans)
        
## 动态规划改进：
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 0:
            return 0
        ans = [0]*len(prices)
        minp = prices[0]
        for i in range(len(prices)):
            if i == 0:
                ans[i] = 0
            else:
                minp = min(minp, prices[i])
                ans[i] = max(ans[i-1], prices[i] - minp)
        return max(ans)

