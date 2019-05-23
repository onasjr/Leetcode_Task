## 不同路径
## m*n方格，即为一共需要走m+n-2步，从中挑出n-1步向下走 即为排列组合问题

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = math.factorial(m+n-2)/math.factorial(n-1)/math.factorial(m-1)

        return ans
