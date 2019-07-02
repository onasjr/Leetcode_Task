## 按奇偶排序数组二
# 分别在奇数和偶数位插入奇数/偶数

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        nums = [0 for _ in range(len(A))]
        
        i = 0
        for v in A:
            if v % 2 == 0:
                nums[i] = v
                i += 2
        
        i = 1
        for v in A:
            if v % 2 == 1:
                nums[i] = v
                i += 2
        
        return nums
