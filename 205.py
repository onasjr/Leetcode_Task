## 同构字符串
# 按坐标位查找后面序列中的该字符，比较当前位在之后序列出现的位置是否相同，不相同则False

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        tmp = True
        for i in range(len(s)): 
            if s[i+1:].find(s[i]) != t[i+1:].find(t[i]):      
                # 比较当前位在之后序列出现的位置是否相同，不相同则False
                tmp = False
                break
        return tmp
