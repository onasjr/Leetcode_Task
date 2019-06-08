## 下一个更大元素②
## 扩展nums为两倍，寻找nums中索引值右边序列中大于该值的值

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums)
        nums2 = nums+nums
        # pdb.set_trace()
        for i, val in enumerate(nums):
            for j in nums2[i+1:]:
                if j > val:
                    res[i] = j
                    break
                else:
                    continue
        return res
