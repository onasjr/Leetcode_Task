## 转换为小写字母
## ord("a") : 得到其ascii序号
## chr(ord("a")+32) : 得到小写字母

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        newstr = ""
        for s in str:
            if s >= "A" and s <= "Z":
                s = chr(ord(s)+32)
            newstr += s
        return newstr
