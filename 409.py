## 最长回文串
## 计算字符出现次数，2的倍数部分全部加入回文串，余下字符最后加一

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        nums = set(s)
        single = []
        for i in nums:
            num = s.count(i)
            if num % 2 == 0:
                res += num
            else:
                res += (num//2)*2
                single.append(1)
        if sum(single) > 0:
            res += 1
        return res
