## 子数组的最小值之和
## 长度可变的滑块，计算min的值，相加（超时）

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ## 双指针，长度可变滑块，计算滑块中最小值
        tmp = []
        for i in range(len(A)):
            for j in range(i, len(A)):
                tmp.append(min(A[i:j+1]))
        return sum(tmp)
        
## 
