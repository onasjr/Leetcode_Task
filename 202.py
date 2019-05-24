## 快乐数
## 递归调用
## 非快乐数会进入死循环

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def eachTime(n):
            length = len(str(n))
            n_str = str(n)
            sum = 0
            if n == 1:
                return True
            if n == 4:    #排除死循环
                return False
            for i in range(length):
                sum += int(n_str[i])**2
            return eachTime(sum)
        ans = eachTime(n)
        return ans
