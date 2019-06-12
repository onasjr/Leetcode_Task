## 两个数组的交集
## 建立set， 查找短set中的数在另一个长set中是否出现

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list1 = list(set(nums1))
        list2 = list(set(nums2))
        l1 = len(list1)
        l2 = len(list2)
        res = []
        if l1 <= l2:
            for i in list1:
                if i in list2:
                    res.append(i)
        else:
            for i in list2:
                if i in list1:
                    res.append(i)
        return res
