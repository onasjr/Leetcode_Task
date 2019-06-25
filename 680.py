## 验证回文字符串二
# 从两端向中间依次比较，如果首尾相同则减一继续，若不同则依次首和尾分别向内一位，比较剩余字符串是否相同

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        i, j = 0, len(s)-1
        
        while i <= j:
            if s[i] == s[j]:
                j -= 1
                i += 1
            else:
                s1 = s[:i]+s[i+1:]
                s2 = s[:j]+s[j+1:]
                if s1 == s[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False
