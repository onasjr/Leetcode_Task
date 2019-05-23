## 完全平方数
## 二分法
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        index1 = 0
        index2 = num/2
        while index1 <= index2:
            mean = (index1 + index2)/2
            if mean**2 > num:
                index2 = mean
            elif mean**2 < num:
                index1 = mean
            else:
                return mean
                


## 利用 1+3+5+7+9+…+(2n-1)=n^2，即完全平方数肯定是前n个连续奇数的和
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum = 1
        i = 1
        while sum < num:
            sum += i + 2
            i += 2
        return sum == num
