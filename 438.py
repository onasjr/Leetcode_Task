## 找到字符串中所有字母异位词
## 滑动框遍历，sorted之后是否相同

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        slen = len(s)
        plen = len(p)
        if slen < plen:
            return []
        p = sorted(p)
        res = []
        for i in range(0, slen - plen + 1):
            if p == sorted(s[i:i+plen]):
                res.append(i)
        return res
        
