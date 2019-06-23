## 非递减数列
## 记录前一个大于后一个的次数，令注意特殊情况，隔位递减

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                ans += 1
                ## [3423]指针指向4时，判断条件
            if i-1 >= 0 and nums[i-1] > nums[i+1] and i+2 < len(nums) and nums[i] > nums[i+2]:
                return False
        return ans <= 1
