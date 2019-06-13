## 整数替换
## 递归调用，每次将次数加1， n分情况


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        def eachTime(n, times, ans):
            if n == 1:
                ans.append(times)
                return times
            else:
                if n % 2 == 0:
                    eachTime(n//2, times+1, ans)
                else:
                    eachTime(n+1, times+1, ans)
                    eachTime(n-1, times+1, ans)
        
        eachTime(n, 0, ans)
        return min(ans)
