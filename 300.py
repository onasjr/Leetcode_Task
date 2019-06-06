## 最长上升子序列
## 动态规划：
## 设置一个list存放截止到第i位上升序列个数

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 1:
            return size
        dp = [1] * size     # 存放截止到该位上升的最大个数
        for i in range(1, size):
            for j in range(0, i):       # 从之前的任意位开始计算上升，可以间断
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)       # 该位上升最大值 = 该位目前值/之前最大值+1
        return max(dp)
