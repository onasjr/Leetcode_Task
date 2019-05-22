## 遍历数组，得到下标i数字，在剩余数组中查找是否含有target-i，返回下标
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans2 = target - nums[i]
            if ans2 in nums[i+1:]:
                ans.append(i)
                ans.append(nums[i+1:].index(ans2) + i + 1)
        return ans
    
num = [2, 7, 11, 15]
target = 9
sol = Solution()
sol.twoSum(num,target)
