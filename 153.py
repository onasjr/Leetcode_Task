## 寻找旋转排序数组中的最小值
## 二分法，设置left right指针，若mid<right则右边顺序，突变在左边，right=mid
## 否则则突变在右边，计算mid和mid+1大小，若在mid后突变则最小，否则left=mid+1

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[0]
