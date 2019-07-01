## 最大连续1的个数二
# 滑块由l和r为首尾，若为0则num+1，若0的个数超过K则从左侧去除0， 将l指针右移，每次更新tmp最大长度

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        tmp, nums, l, r = 0, 0, 0, 0
        for r, item in enumerate(A):
            if item == 0:
                nums += 1
            while nums > K:
                if A[l] == 0:
                    nums -= 1
                l += 1
            
            tmp = max(tmp, r-l+1)
        return max(tmp, r-l+1)
