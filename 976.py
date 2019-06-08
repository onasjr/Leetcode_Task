## 三角形的最大周长
## 降序排列，依次另最大值为第三边，次小两个值为1和2，判断是否满足1+2>3

class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        i = 0
        A = A[::-1]
        all = []
        while i <= len(A)-3:
            if A[i+2] + A[i+1] > A[i]:
                return sum(A[i:i+3])
            i += 1
        return 0
