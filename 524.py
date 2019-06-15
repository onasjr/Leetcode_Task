## 通过删除字母匹配到字典里最长单词
## 对字典串中单词按顺序依次比较，如ale，比较s中是否按顺序存在这几个字母，以i记录检索到的长度


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        # 对字典串按长度降序排列
        d.sort(key = lambda x: len(x), reverse = True)
        
        # 对字典串中单词按顺序依次比较，如ale，比较s中是否按顺序存在这几个字母，以i记录检索到的长度
        for word in d:
            i = 0
            for num in s:
                if num == word[i]:
                    i += 1
                if i == len(word):
                    return word
        return ""
