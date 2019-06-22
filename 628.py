## 三个数的最大乘积
## 计算两最小一最大乘积（负负正），三最大乘积，比较

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans1 = nums[0]*nums[1]*nums[-1]
        ans2 = nums[-1]*nums[-2]*nums[-3]
        return max(ans1, ans2)
