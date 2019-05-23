## 跳跃游戏
## 记录在当前位置所对应最大跳跃步长下，每跳跃一步所对应的最远距离，若>=length-1则True

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        start = 0
        end = 0
        n = len(nums)
        while start <= end and end < n - 1:
            end = max(end, start + nums[start])
            start += 1
        return end >= n-1
