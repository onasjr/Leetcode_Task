## Fizz Buzz
## 循环，查找3和5的倍数

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 0
        res = [str(i) for i in range(1, n+1)]
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                res[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                res[i-1] = "Fizz"
            elif i % 5 == 0:
                res[i-1] = "Buzz"
            else:continue
        return res
