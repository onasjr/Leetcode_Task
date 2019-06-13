## 判断子序列
## 遍历字符串s中的字符是否在t中出现，若出现则将start重置，继续查找start后面的字符串

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        for i in range(len(s)):
            alpha = s[i]
            sub_t = t[start:]
            index = sub_t.find(alpha)
            if index == -1:         # 查找t的剩余字符串中是否存在
                return False
            else:
                start += (index + 1)        # 后续检索开始的位置
        return True
