## 重复的DNA序列
## 建立dict，遍历str，将序列保存为key，出现次数保存为value；
## 注意：调用dict.get（key， 0）  ： 未出现值默认添加

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = {}
        if len(s) <= 10:
            return None
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            res[tmp] = res.get(tmp, 0) + 1
        return [i for i in res.keys() if res[i] >= 2]
