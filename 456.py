## 132模式

## (超时)
## 查找每个数左边第一个比他大的数，在该数左边查找最小的数，比较最小的数是不是比原数小
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) < 3:
            return False
        index2, index3 = 0, 0
        for i in range(1, len(nums)):
            for j in range(len(nums[:i]), 0, -1):
                if nums[j] > nums[i]:       #左边存在比他大的元素，第一个
                    index2 = j
                    index3 = i
                    break
            if index2 != 0:
                tmp = min(nums[:index2])
                if tmp < nums[index3]:
                    return True
        return False
        
        
## 倒序，将当前数入栈，保存仅小于该数值的数为min，如果下一个数比min小即为T
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        _MIN = float('-inf')
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < _MIN:
                return True
            while stack and nums[i] > stack[-1]:
                _MIN = stack.pop()
            stack.append(nums[i])
            
        return False
