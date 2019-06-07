## 最长重复子数组
## 动态规划
## dp[i][j]代表以A[i-1]与B[j-1]结尾的公共字串的长度,公共字串必须以A[i-1]，B[j-1]结束，即当A[i-1] == B[j-1]时，dp[i][j] = dp[i-1][j-1] + 1; 
当A[i-1] != B[j-1]时，以A[i-1]和B[j-1]结尾的公共字串长度为0,dp[i][j] = 0

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len_A, len_B= len(A), len(B)
        dp = [[0]*(len_B+1)]*(len_A+1)
        maxlen = 0
        for i in range(1,len_A+1):
            for j in range(1,len_B+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1       # 以A[i-1]和B[j-1]结尾的公共子串长度
        return max(max(dp))
