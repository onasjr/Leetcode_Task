## 最长回文字符串
## 以每个字符为中心字符，分为奇数偶数情况依次左右移动jk坐标，更新相等部分最大值

class Solution:
    def longestPalindrome(self, s):
        """
        :param s:
        :return:
        """
        n = len(s)
        count = 0   # 记录最大长度
        res = ""

        for i in range(n):
            # 奇数
            j, k = i, i
            while j >= 0 and k <= n-1:
                if s[j] == s[k]:
                    if k - j + 1 > count:
                        count = k - j + 1
                        res = s[j:k+1]
                    j -= 1
                    k += 1
                else:break
            # 偶数
            j, k = i, i+1
            while j >= 0 and k <= n-1:
                if s[j] == s[k]:
                    if k - j + 1 > count:
                        count = k - j + 1
                        res = s[j:k+1]
                    j -= 1
                    k += 1
                else:break
        return res
