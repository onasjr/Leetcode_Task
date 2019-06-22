## 子数组最大平均数一
## 滑动窗口计算

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = sum(nums[:k])
        res = tmp
        for i in range(0, len(nums)-k):
            tmp = tmp - nums[i] + nums[i+k]
            res = max(tmp, res)
        return res/k        
