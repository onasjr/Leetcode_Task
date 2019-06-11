## 打家劫舍 II
## 递归，当前位和上一位最大值；
## 分为两个情况：取第一位和取最后位

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l <= 2 and l > 0:
            return max(nums)
        ## 分两种情况，从第一个开始和取最后一个
        nums1 = nums[:l-1]
        nums2 = nums[1:]

        def eachtime(nums):
            last = 0        # 上一位以前最大值
            now = 0     # 该位最大值
            for i in nums:
                last, now = now, max(last+i, now)
            return now

        ans1 = eachtime(nums1)
        ans2 = eachtime(nums2)
        return max(eachtime(nums1), eachtime(nums2))
