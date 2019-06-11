## 最大单词长度乘积
## 得到每项字母不重复sets
## 双层循环依次比较sets[i] sets[j]与之后的相同项，若无，更新长度最大值

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        res = 0
        sets = [set(i) for i in words]
        for i in range(n):
            for j in range(i+1, n):
                if not sets[i] & sets[j]:       # 返回相同项
                    res = max(res, len(words[i]) * len(words[j]))
        return res
