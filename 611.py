## 有效的三角形个数
## 排序，从大到小遍历，令最大值为三角形一条边，从左到右查找能构成三角形的最小边

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res= 0
        ## 从大到小遍历
        for i in range(len(nums)-1, 1, -1):
            # 令最大值左边为三角形一条边，从左到右查找能构成三角形的最小边
            l, r = 0, i-1
            while l < r:
                if nums[l]+nums[r] > nums[i]:
                    res += r-1-l+1
                    r -= 1
                else:
                    l += 1
        return res
