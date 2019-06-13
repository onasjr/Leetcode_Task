## 等差数列划分
## 动态规划，dp[i]表示以第i为结尾的等差数列个数


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ## 动态规划，dp[i]表示以第i为结尾的等差数列个数
        dp = [0 for i in range(len(A))]

        for i in range(2, len(A)):
            if A[i - 1] - A[i - 2] == A[i] - A[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0

        return sum(dp)
