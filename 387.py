## 字符串中的第一个唯一字符
## dict存储，找到value为1的key


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        res = []
        for i in s:
            dict[i] = dict.get(i, 0) + 1
        for k, v in dict.items():
            if v == 1:
                res.append(s.index(k))
        if res == []:
            return -1
        else:
            return min(res)
