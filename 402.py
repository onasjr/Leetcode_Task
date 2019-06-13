## 移掉K位数字
## 寻找后一位比前一位大的删除
## 注意首位为零的情况

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"

        j = 0
        num = list(num)

        for i in range(k):
            while j < len(num) - 1 and num[j] <= num[j + 1]:
                j += 1

            num.pop(j)
            j = max(0, j - 1)

        while len(num) > 0 and num[0] == "0":
            num.pop(0)
        
        if len(num) == 0:
            return "0"
        return "".join(num)
