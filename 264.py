## 丑数2
## 三指针，排除重复项
## 依次在数列中加入2,3,5倍数的最小值

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        res = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        while len(res) < n:
            ans = min(res[index2]*2, res[index3]*3, res[index5]*5)
            res.append(ans)
            if res[-1] == res[index2] * 2:
                index2 += 1
            elif res[-1] == res[index3] * 3:
                index3 += 1
            elif res[-1] == res[index5] * 5:
                index5 += 1
            if res[-1] == res[-2]:
                res.pop()
                i -= 1
            else:
                i += 1
        return res[-1]
