## 随机数索引
## 遍历将位置存储在list中，产生随机数返回其中一个

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = []
        for i, v in enumerate(self.nums):
            if v == target:
                res.append(i)
        index = random.randint(0, len(res)-1)
        return res[index]
        
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
