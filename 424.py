## 替换后的最长重复字符串
# 滑动窗口，l为最长子序列左边界，r为最长子序列右边界

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, r, dict = 0, 0, {}
        # l为最长子序列左边界，r为最长子序列右边界
        while r < len(s):
            # r为新遍历到的字符， 将其出现次数存入dict
            dict[s[r]] = dict.get(s[r], 0) + 1
            # 当l到r中字符总数-出现次数最大的字符数量>k：l右移, 将该字符出现次数-1
            if sum(dict.values()) - max(dict.values()) > k:
                dict[s[l]] -= 1
                l += 1
            r += 1
        return r-l
