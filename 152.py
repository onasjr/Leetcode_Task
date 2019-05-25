## 乘积最大子序列
## 直接遍历，两个指针，一个记录起始位置一个记录终止位置（暴力法耗时长）

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        index1 = 0
        index2 = len(nums)-1
        for i in range(len(nums)):
            res.append(nums[i])
            if nums[i] == 0:
                continue
            nums2 = nums[i+1:]
            ans = nums[i]
            for j in range(len(nums2)):
                if nums2[j] == 0:
                    break
                else:
                    ans *= nums2[j]
                    res.append(ans)
        # pdb.set_trace()
        if not res:
            return 0
        else:
            return max(res)
            
## 动态规划，存储每个位置可能的最大正值和最小负值
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        ans = [0]*2     # [最小负值， 最大正值]
        if nums[0] >= 0:
            ans = [0, nums[0]]
        else:
            ans = [nums[0], 0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:        # 若当前位置为正，则更新当前位置对应ans
                ans = [ans[0]*nums[i], max(nums[i], ans[1]*nums[i])]
            else:
                ans = [min(ans[1]*nums[i], nums[i]), nums[i]*ans[0]]
            res = max(ans[1], res)      # 记录截止到当前位置上的最大值
        return res
