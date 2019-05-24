## 翻转字符串里的单词
## 拆分为list，再转换为str

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s.split()
        ans_reverse = ans[::-1]
        if len(ans_reverse) == 0:
            return ""
        res = ans_reverse[0]
        for i in range(1, len(ans)):
            res += " "
            res += ans_reverse[i]
        return res
