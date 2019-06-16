## 反转字符串 II
## 从0到len（s），间隔为2k翻转

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        
        for i in range(0, len(s), 2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)
