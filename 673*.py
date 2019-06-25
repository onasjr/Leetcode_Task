## 最长递增子序列的个数
## 动态规划：同300题思路，dp[i]为以第i为结尾的子序列长度，建立count[i]表示以第i位结尾的最长子序列个数，
## 之后根据dp中获得的最长长度所对应索引值获取个数，求和

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lll = len(nums)
        if lll <= 1:
            return lll
        dp = [0] * lll
        count = [1] * lll   # 以第i位截止的最长递增子序列个数

        for i in range(1, lll):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] <= dp[j]:  # 以第i位为结尾可与前一位形成递增序列
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:  # 以第i位为结尾已存在一个递增序列
                        count[i] += count[j]

        maxlen = max(dp)
        res = 0
        for i in range(len(dp)):
            if dp[i] == maxlen:
               res += count[i]
        return res
