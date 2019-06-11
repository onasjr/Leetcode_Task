## 存在重复元素三
## 设置start和end滑块，比较差值；
## 超时T_T

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        l = len(nums)
        start = 0
        for start in range(0, l):
            for end in range(start+1, start + k+1):
                if end < l:
                    if abs(nums[start] - nums[end]) <= t:
                        return True
        return False
