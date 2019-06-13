## 第三大的数
## 排序，设置start表示当前数据是第几大，注意相同时


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(list(set(nums))) <3:
            return max(nums)
        ans = 0
        nums.sort(reverse = True)
        start = 1
        for i in range(1, len(nums)):
            if start < 3 and nums[i] != nums[i - 1]:
                start += 1
            elif start < 3 and nums[i] == nums[i - 1]:
                continue
            if start == 3:
                ans = nums[i]
                break
        return ans
