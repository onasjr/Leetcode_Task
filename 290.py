## 单词规律
## 比较pattern中相同项对应下标在s中是否相同

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if str.count(" ") != len(pattern) -1:
            return False
        s = str.split(" ")
        # pdb.set_trace()
        for i in range(1,len(pattern)):
            for j in range(0,i):
                if pattern[i] == pattern[j]:
                    if s[i] != s[j]:
                        return False
                    break
                else:
                    if s[i] == s[j]:
                        return False
        return True
