## 无重复字符的最长子串
## 用set建立滑动窗口，

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left = 0
        maxlen = 0
        curlen = 0
        lookup = set()  # 滑动窗口

        for i in range(len(s)):
            curlen += 1
            # 先判断s[i]是否已在窗口中
            #若在，则把窗口中的相同字符串移走，再把该字符放入窗口中
            while s[i] in lookup:
                lookup.remove(s[left])  # 因为集合是无序的，想要移除窗口中最左边的元素，需要用一个left变量来实现
                left += 1
                curlen -= 1     # 窗口长度
            if curlen > maxlen:     # 更新窗口最大长度
                maxlen = curlen
            lookup.add(s[i])
        return maxlen
