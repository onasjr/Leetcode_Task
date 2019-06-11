## 存在重复元素 II
## 设置长度最大为k的滑块，比较首尾字符
## start和end（超时）


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = len(nums)
        start = 0
        for start in range(0, l):
            for end in range(start+1, start + k+1):
                if end < l:
                    if nums[start] == nums[end]:
                        return True
        return False
