## 滑动窗口中位数
## 设置k长度窗口，分为奇数偶数分别计算

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res = []
        if len(nums) < k:
            return None
        for i in range(len(nums) - k+1):
            tmp = sorted(nums[i:i + k])
            if k % 2 == 0:
                j = int(k / 2) - 1
                res.append((tmp[j] + tmp[j+1])/2)
            else:
                j = int(k / 2)
                res.append(tmp[j])
        return res
