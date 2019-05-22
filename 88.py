## 合并两个有序数组
## 数组拼接，sorted排序

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[0:m+n] = sorted(nums1[0: m] + nums2)
        return nums1
