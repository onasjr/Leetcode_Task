## 罗马数字转整数
## 1.建立dictionary
## 2.遍历字符串中字符
## 3.去除最后一项：比较当前与后一个所对应数字大小，大则加，小则减
## 4.加上最后一项

class Solution:
    def romanToInt(self, s):
        ans = 0
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for i,char in enumerate(s[:-1]):
            if dic[char] >= dic[s[i+1]]:
                ans += dic[char]
            else:ans -= dic[char]
        ans += dic[s[-1]]
        return ans
