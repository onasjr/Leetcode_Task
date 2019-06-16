## 反转字符串中的单词 III
## split将单词分离，依次翻转


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        ans = ""
        for i in words:
            ans += i[::-1] + " "
        return ans[:-1]
