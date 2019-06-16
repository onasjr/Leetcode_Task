## 最优除法
## 只有当被除数最小才可以得到最大值，因此应从第二位开始优先计算知道末尾


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 0:
            return ""
        elif len(nums) == 2:
            return ""+ str(nums[0]) + "/" + str(nums[-1])
        res = ""+str(nums[0]) + "/("
        for i in range(1, len(nums)-1):
            res += str(nums[i]) + "/"
        res += str(nums[-1]) + ")"
        return res
