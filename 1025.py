## 除数博弈
# 当N为奇数，其因数也一定是奇数，那么alice选过之后剩下为偶数，bob只需一直选1，保证alice遇到奇数，则取胜；
# 当N 为偶数，则alice可一直选1， 使得bob拿到都是奇数， 则alice取胜

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0
