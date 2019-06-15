## 连续的子数组和
## 当长度<2，肯定无法组成；之后设置i和j表示开始和结束，依次记录从第一个数开始2,3,4长度，第二个数开始2,3··等的和，满足条件返回

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        l = len(nums)
        if l < 2:
            return False
        
        for i in range(0, l-1):
            sums = nums[i]
            for j in range(i+1, l):
                sums += nums[j]
                if k == sums == 0:
                    return True
                elif k != 0 and sums % k == 0:
                    return True
        return False
