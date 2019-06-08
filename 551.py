##学生出勤记录 I
## 查找LLL和A个数

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"A": 0, "LLL": 0}
        if len(s) <= 3:
            if "LLL" in s:
                return False
            elif s.count("A") >= 2:
                return False
            else:
                return True
        if s[-3:] == "LLL":
            return False
        for i in range(len(s)-3,len(s)):
            if s[i] == "A":
                dict["A"] += 1
        for i in range(len(s)-3):
            if s[i] == "A":
                dict["A"] += 1
            if s[i] == s[i + 1] == s[i + 2] == "L":
                dict["LLL"] += 1
                i += 1
        if dict["A"] <= 1 and dict["LLL"] == 0:
            return True
        else:
            return False
