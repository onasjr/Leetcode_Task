## 买卖股票的最佳时机2
## 默认当天可以买卖，则见峰谷差则计算为收益

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pro = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                pro += diff
        return pro
