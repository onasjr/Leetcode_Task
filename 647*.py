## 回文子串
## # dp[i]为以第i为结尾的回文串个数，双层循环，一层i表示结尾位，一层j向前遍历表示起始位

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isSub(nums):
            return nums == nums[::-1]
        
        if not s:
            return 0
        
        ll = len(s)
        dp = [0 for i in range(ll)]
        dp[0] = 1
        
        for i in range(1, ll):
            for j in range(i, -1, -1):
                if isSub(s[j:i+1]):
                    # dp[i]为以第i为结尾的回文串个数
                    dp[i] += 1
                    
        return sum(dp)
