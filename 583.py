## 两个字符串的删除操作
## 动态规划，dp[i][j]为截止到word1和word2的第i，j位的字符串最大公共子串结果，实际为寻找最大公共子串的过程

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ## 找word1和word2的最长公共子序列
        
        dp = [[0 for i in range(len(word1)+1)] for i in range(len(word2)+1)]
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return len(word1)+len(word2)-2*dp[-1][-1]
