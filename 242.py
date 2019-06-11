## 有效的字母异位词
## 字母异位词：字母交换位置，因此对其排序比较


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(list(s)) == sorted(list(t))
