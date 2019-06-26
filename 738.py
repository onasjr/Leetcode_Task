## 单调递增的数字
## # 从后往前遍历，若前一位大于后一位，则本位-1，后面全部为9,最后处理高位
        # 特殊情况：10以内数字

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 从后往前遍历，若前一位大于后一位，则本位-1，后面全部为9,最后处理高位
        # 特殊情况：10以内数字
        strN = str(N)
        lll = len(strN)
        if N <= 10:
            return N - 1

        for i in range(lll-1, 0, -1):
            if strN[i-1] > strN[i]:
                strN = ""+strN[:i-1]+str(int(strN[i-1])-1)+"9"*(lll-i)
        return int(strN)
