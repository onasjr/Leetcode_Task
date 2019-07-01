## 最长湍流子数组
# 

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lll = len(A)
        # 初始化ans，若相邻数不相等，则后一个为2， 否则为1
        ans = [1 for i in range(lll)]
        for i in range(1, lll):
            if A[i] != A[i-1]:
                ans[i] = 2
                
        if lll == 2:
            return ans[-1]
        
        # 在2~lll-1， 比较i及前两个数是否满足峰/谷关系，若满足则ans[i]=ans[i-1]+1
        for i in range(2, lll):
            if (A[i - 1] > A[i] and A[i - 1] > A[i - 2]) or (A[i - 1] < A[i] and A[i - 1] < A[i - 2]):
                ans[i] = ans[i - 1] + 1

        return max(ans)
