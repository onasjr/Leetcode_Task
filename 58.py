## 最后一个单词的长度
## 思路：split函数分割str为list，选取其中最后一个list

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if not s:
            return 0
        return len(s[-1])
