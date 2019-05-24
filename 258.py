## 各位相加
## 递归调用，每次计算一次结果
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def eachTime(num):
            sum = 0
            # pdb.set_trace()
            n = len(str(num))
            if n == 1:
                return num
            else:
                tmp = str(num)
                for i in range(n):
                    sum += int(tmp[i])
                return eachTime(sum)
        ans = eachTime(num)
        return ans
