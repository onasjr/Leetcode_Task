## 滑动窗口最大值
## 直接遍历，注意特殊情况nums为空或k= 0

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return None
        if k == 0:
            return None
        l = len(nums)
        res = [0]
        for i in range(l - k + 1):
            res.append(max(nums[i:i+k]))
        if len(res) > 1:
            return res[1:]
        else:return [0]
