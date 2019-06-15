## 预测赢家
## 偶数赢，奇数dp（不会做）


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n % 2 == 0:      # 如果n为偶数则必定会赢
            return True
        
        ## 初始化dp，对于dp对角线初始化为nums
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        
        
        for l in range(1,n):
            for i in range(n):
                j = i+l
                if j<n:
                    dp[i][j] = max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
        return dp[0][n-1]>=0           
