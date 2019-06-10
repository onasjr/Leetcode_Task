## 寻找旋转排序数组中的最小值 II
## 二分法，不断去掉重复项，若right<mid，则旋转出现在右边，更新left = mid+1；else：right=m

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] == nums[left+1]:
                left += 1
            elif nums[right] == nums[right-1]:
                right -= 1
            else:
                m = (left+right) // 2
                if nums[right] < nums[m]:
                    left = m + 1
                else:
                    right = m
        return nums[left]
