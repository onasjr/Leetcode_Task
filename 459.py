## 重复的子字符串
## 查找前i（i<ln/2）位，比较是否在整体中出现个数与此次相同


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        for i in range(l/2):
            # pdb.set_trace()
            tmp = s[0:i+1]
            if s[i+1] == tmp[0]:
                num = s.count(tmp)
                if num * len(tmp) == l and num != 1:
                    return True
        return False
