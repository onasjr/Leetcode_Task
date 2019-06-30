## 石子游戏
# 动态规划：dp[i][j]表示从i到j堆之间的最大绝对差值
# 转移方程：dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        ## dp[i][j]为从i到j取石子可以得到的最差值分数， +则alex赢分
        # 转移方程：dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        # 含义：第i到j堆的最大差值即为先取首和先取尾之后剩余部分最大值的差值
        lll = len(piles)
        dps = [[0 for i in range(lll)] for j in range(lll)]
        # dps对角线存储当前第i个的石子数
        for i in range(lll):
            dps[i][i] = piles[i]
            
        
        # 从2堆开始计算
        for d in range(1, lll):
            # 有这些组需要比较
            for j in range(lll-d):
                dps[j][d+j] = max(piles[j]-dps[j+1][d+j], piles[d+j]-dps[j][d+j-1])
        
        return dps[0][lll-1]>0
                
