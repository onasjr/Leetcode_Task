## 找到所有数组中消失的数字
## 调用set（存在额外空间）

class Solution:
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]
        
        
