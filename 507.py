## 完美数
## 每位计算

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        ans = []
        ans.append(1)
        mid = int(num**0.5)
        i = 2
        while i <= mid:
            if num % i == 0:
                ans.append(i)
                ans.append(num/i)
            i += 1
        return sum(ans) == num
