## 长度最小的子数组
## 设定start表示滑动框首坐标，j为尾坐标，计算达到allsum>s的位置，
## 之后在保证大于情况下依次后移start，直到res最小

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        start, allsum, res = 0, 0, float("inf")
        for j in range(len(nums)):
            allsum += nums[j]
            while allsum >= s:
                res = min(res, j - start + 1)   # 更新长度
                allsum -= nums[start]           # 减去start起始数
                start += 1
        if res == float("inf"):
            return 0
        else:
            return res
