## 实现一个魔法字典
## 查找长度相同项存入list，在该list中查找只差一个字母的项，并将每个list中单词的相差字母个数存入res[]
## 若res中存在1则T

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        self.dict = [i for i in dict]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        ans = []
        n = len(word)
        dict = self.dict
        for k in dict:
            if len(k) == len(word):
                ans.append(k)
        flag = []
        for k in ans:
            flag.append(0)
            for i in range(n):
                if k[i] != word[i]:
                    flag[-1] += 1
        if 1 in flag:
            return True
        else:
            return False
