## 两个数组的交集 II
## 查找短数组中数字是否在长数组中出现，若出现则删除

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        res = []
        if l1 <= l2:
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    res.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    nums1.remove(i)
                    res.append(i)
        return res
