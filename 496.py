## 下一个更大元素 I
## 依次在nums2中寻找nums1中数字的位置及右边序列中第一个增长值
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums1)
        for i, val in enumerate(nums1):
            index2 = nums2.index(val)
            for j in nums2[index2+1:]:
                if j > val:
                    res[i] = j
                    break
                else:
                    continue
        return res
