## 验证回文串
## 使用filter过滤掉非字母字符，对其统一大小写，验证翻转前后是否相等

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(filter(str.isalnum, str(s))).upper()
        # pdb.set_trace()
        return s == s[::-1]
