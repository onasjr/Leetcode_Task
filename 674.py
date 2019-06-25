## 最长连续递增序列
## dp动态规划，dp[i]为截止到第i位最长连续子序列的长度

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        lll = len(nums)
        if lll == 0:
            return 0
        if lll == 1:
            return 1
        dp = [0 for i in range(lll)]
        dp[0] = 1
        for i in range(1, lll):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        return max(dp)
