## 逆序遍历，删除等于val的项

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tmp = len(nums)-1
        while tmp >= 0:
            if nums[tmp] == val:
                nums.remove(nums[tmp])
            else:tmp-=1
        return len(nums)

nums = [3,2,2,3]
ans = Solution().removeElement(nums,2)
print(ans)
