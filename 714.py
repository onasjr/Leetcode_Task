##  买卖股票最佳时期
## 思路：
设置两个状态转移方程
cash表示手上没有股票时的利润
hold表示手上有股票时的利润
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(len(prices)):
            cash = max(cash, hold+prices[i]-fee)
            hold = max(hold, cash-prices[i])
        return cash
