## 两个矩形面积-相交部分面积
## 判断是否相交，计算重叠边长

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        ## 两个矩形面积-相交部分面积
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        ## 当两个矩形横向存在重叠
        if E < C and G > A:
            w = min(C, G) - max(A, E)
        else:
            w = 0
        
        ## 当两个矩形纵向重叠
        if F < D and H > B:
            h = min(D, H) - max(B, F)
        else:
            h = 0
        s3 = w * h
        return s1 + s2 - s3
        
