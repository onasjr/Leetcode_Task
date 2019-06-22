## 错误的集合
## 计算set的和，1~n的和，与S做差

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        Smiss = sum(set(nums))
        Sn = len(nums)*(len(nums)+1)//2
        return [sum(nums)-Smiss, Sn-Smiss]
