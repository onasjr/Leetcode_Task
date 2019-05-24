## 词典中最长的单词
## 在排序后的list中寻找末尾加一个字母的连续子列末端，起始位置依次由数列任意位开始
## 寻找到的子列放入res中，比较res每一行末位在原数列中的位置，最小的即为最后结果


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words1 = copy.copy(words)
        words1.sort()

        i = 0
        if len(words1) == 1:
            return words1[0]
        res = []
        for m in range(len(words1)):
            words2 = words1[m:]
            ans = []
            for i in range(len(words2)-1):
                if words2[i] == words2[i + 1][:-1]:
                    ans.append(words2[i+1])
                else:
                    break
            if ans != []:
                res.append(ans)
        index = 10000
        for i in range(len(res)):
            index = min(words.index(res[i][-1]), index)
        return words[index]
