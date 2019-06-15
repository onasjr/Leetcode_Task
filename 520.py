## 检测大写字母
## 分别检查是否全为大写/小写；再检查是否第一个字母大写其他小写，若不是，则返回


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
