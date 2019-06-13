## 字符串中的单词数
## 在末尾补空格，数空格数量

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += " "
        num = 0
        for i in range(1,len(s)):
            if s[i] == " " and s[i-1] != " ":
                num += 1
        return num
        
