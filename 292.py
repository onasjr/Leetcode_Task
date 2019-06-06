## Nim 游戏
## 4的倍数False

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n%4 == 0:
            return False
        else:
            return True
