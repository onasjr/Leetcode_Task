## 猜数字大小
## 二分查找

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low <= high:
            mid = (low + high) / 2
            tag = guess(mid)
            if tag == 1:
                low = mid + 1
            elif tag == -1:
                high = mid - 1
            else:
                return mid
