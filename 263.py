## 丑数
## 递归是否是235倍数
## 注意排除0

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def eachTime(num):
            if num == 0:
                return False
            if num == 1:
                return True
            for i in [2,3,5]:
                if (num%i) == 0:
                    return eachTime(num/i)
            else:
                return False
        ans = eachTime(num)
        return ans
