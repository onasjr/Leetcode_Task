## 公平的糖果交换
## 计算数组差值/2，查找A中i是否由i+差值/2在B中

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        suma = sum(A)
        sumb = sum(B)
        setA = set(A)
        setB = set(B)
        if sumb > suma:
            diff = int((sumb - suma) / 2)
            for item in setA:
                if item+diff in setB:
                    return [item, item+diff]
        else:
            diff = int((suma - sumb) / 2)
            for item in setB:
                if item+diff in setA:
                    return [item+diff, item]
