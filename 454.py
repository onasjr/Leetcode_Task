##四数相加 II
## 计算A和B中的两两相加结果，存储在dict中出现的次数
## 计算C和D中相加结果，若与dict中互补，则次数加上该key的value

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        dict = {}
        
        for a in A:
            for b in B:
                dict[a+b] = dict.get(a+b, 0) + 1
        
        for c in C:
            for d in D:
                s = -(c+d)
                if s in dict:
                    count += dict[s]
        return count
