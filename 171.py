## Excel表序号
## 26进制转十进制
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x) - ord('A') + 1
        return ans
