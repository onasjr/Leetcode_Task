## 重塑矩阵
## 将矩阵展开为一维，之后根据行数重组


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r = int(r)
        c = int(c)
        a = []
        b = []
        
        for i in nums:
            for j in num:
                a.append(i)
        
        if le(a) != r*c:
            return nums
        else:
            for i in range(r):
                b.append(a[i*c:(i+1)*c])
            return b
