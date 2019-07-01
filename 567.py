## 字符串的排列
# 滑动窗口依次比较排序后的s1和s2中相同位数排序后的值，若相等则返回T（超时）

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        tem = sorted(s1)
        lll = len(tem)
        for i in range(len(s2)):
            if s2[i] in tem:
                if sorted(s2[i:i+lll]) == tem:
                    return True
        return False
        

# 建立dict存储s1中数字出现次数， dict2存储s1长度内数字出现次数，若二者相等，则T；
# 否则dict2中第一个记录的出现次数-1；更新dict2

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        tmp = set(list(s1))
        lll = len(s1)
        if lll >= len(s2):
            return sorted(s1) == sorted(s2) 
        dict = {}
        for i in tmp:
            dict[i] = dict.get(i, 0) + s1.count(i)

        dict2 = {}
        for i in range(0, lll):
            dict2[s2[i]] = dict2.get(s2[i], 0) + 1
        for i in range(lll, len(s2)+1):

            if dict == dict2:
                return True
            elif i == len(s2):
                return False
            else:
                if dict2[s2[i - lll]] != 1:
                    dict2[s2[i - lll]] -= 1
                else:
                    del dict2[s2[i - lll]]
                dict2[s2[i]] = dict2.get(s2[i], 0) + 1
        return False
