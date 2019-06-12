## 赎金信
## 使用set，之后判断是否存在相应字符，比较数量是否满足

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if i not in magazine or magazine.count(i) < ransomNote.count(i):
                return False
        return True
