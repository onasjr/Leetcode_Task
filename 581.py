## 最短无序连续子数组
## 排序，比较不同位

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortednums = sorted(nums)
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2 and sortednums[p1] == nums[p1]:
            p1 += 1
        while p1 <= p2 and sortednums[p2] == nums[p2]:
            p2 -= 1
        return p2 - p1 +1
