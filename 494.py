## 目标和
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ## 0/1背包问题；首先将整个nums和分为正数和部分、负数和部分，那么sum(nums) = sum(N)+sum(P);
        ## sum(P) - sum(N) = target, 等式两边同时加上sum(P)和sum(N), 化简后可得(sum(nums) + target)/2=sum(P)
        ## 之后即可化为0/1背包问题，使用动态规划dp，dp[i]即为组成i的可能性
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P,num-1,-1):dp[j] += dp[j - num]
        return dp[P]
