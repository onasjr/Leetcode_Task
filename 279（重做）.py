## 完全平方数
## 动态规划

import math

#f(12) = min(f(1), f(4), f(9)) + 1

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_num = int(math.floor(n ** 0.5))
        # 列出符合条件的完全平方数
        nums = [i*i for i in range(1, max_num + 1)]
        
        dp = dict()
        dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n + 1):
            count = float('inf')
            for num in nums:
                if i - num >= 0:
                    count = min(count, dp[i - num] + 1)
                else:
                    break
            dp[i] = count
            
        return dp[n]
