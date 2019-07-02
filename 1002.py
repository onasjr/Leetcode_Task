## 查找常用字符
# 记录A中第一个单词中个字母，以此为对照，查找在其他所有单词中这些字母出现的最小值，更新res

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        if not A:
            return res

        key = set(A[0])

        for i in key:
            # 遍历key中字符，查找在所有单词中字幕出现的次数最小值，更新
            minnum = min(j.count(i) for j in A)
            res += minnum * i

        return res
