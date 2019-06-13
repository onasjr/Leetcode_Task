## 分割等和子集
## 递归，分奇数偶数，当结果递归结果为True返回True


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        all = sum(nums)
        if all % 2 == 1:
            return False
        half = all//2
        nums.sort()
        res = False
        
        def eachTime(nums, target):
            if target < 0:
                return
            if target == 0:
                return True
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    if eachTime(nums[:i] + nums[i + 1:], target - nums[i]):
                        return True
            return False

        return eachTime(nums, half)
