## 4的幂
## 转为2进制，100,10000,1000000····
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        tmp = bin(num)
        if tmp[2] == "1" and "1" not in tmp[3:] and len(tmp[3:]) % 2 == 0:
            return True
        else:
            False
