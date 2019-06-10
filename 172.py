## 阶乘后的零
## 一个2和一个5产生一个0，因此需要找到一共有多少个5,25为5*5，相当于2个;10=2*5相当于1个


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        count = 0
        while n >= 5**k:
            count += n//(5**k)
            k += 1
        return count
