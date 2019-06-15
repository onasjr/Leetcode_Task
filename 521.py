## 最长特殊序列 Ⅰ
## 分析：如果a和b相同，则不存在特殊序列；如果不等，则返回长度长的字符串，因为该字符串不可能在b中出现


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))
