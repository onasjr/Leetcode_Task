## 七进制数
## 除以7取余，更新num为商

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 去除符号位
        if num < 0:
            flag = "-"
            num = -num
        else:
            flag = ""

        if num == 0:
            return "0"

        res = []
        while num != 0:
            res.append(num % 7)
            num = num // 7
        res = res[::-1]
        for i in res:
            flag += str(i)
        return str(flag)
