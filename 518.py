##
## dp动态规划：将目标金额0~amout建立的dp表，eg：对硬币遍历，如存在硬币为1，金额为5，则可以分为金额为1和金额为4的和，依次计算

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ## dp[i]为金额为i时组合的可能性
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for i in coins:
            for j in range(1, amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[amount]
