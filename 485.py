## 最大连续1的个数
## 查找相邻位，保存连续个数为list

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        ans.append(0)
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if i == len(nums)-1:
                    ans.append(tmp+1)
                else:
                    tmp += 1
            elif nums[i] != 1:
                ans.append(tmp)
                tmp = 0
        return max(ans)
