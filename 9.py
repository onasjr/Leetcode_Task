## 负数必定不满足回文数，排除
## 其次将int转换为str，用切片翻转，与原str比较

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x_reverse = str(x)[::-1]
            if x_reverse == str(x):
                return True
            else:
                return False
