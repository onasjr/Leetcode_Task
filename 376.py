## 摆动序列
## 记录上升序列和下降序列up和down，当序列上升up = down  + 1;反之：down = up + 1

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 2:
            return l
        up, down = 1, 1
        for i in range(1, l):
            if nums[i] > nums[i-1]:
                up = down +1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)
