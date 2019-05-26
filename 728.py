## 自除数
## 遍历每一位记录是否整除

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for n in range(left, right+1):
            ans.append(n)
            i = 0
            while i < len(str(n)):
                # pdb.set_trace()
                if int(str(n)[i]) == 0:
                    ans.pop()
                    break
                elif n % int(str(n)[i]) == 0:
                    i += 1
                else:
                    ans.pop()
                    break
        return ans
