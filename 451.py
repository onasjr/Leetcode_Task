## 根据字符出现频率排序
## 将出现字符和次数存储在dict，之后对其values值对items排序

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0) + 1

        ans = ""
        dict = sorted(dict.items(), key = lambda d:d[1], reverse=True)

        for i in dict:
            ans += i[0]*i[1]

        return ans
