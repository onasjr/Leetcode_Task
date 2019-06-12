## 打乱数组
## random.shuffle() 随机打乱一组数据

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.initial = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.initial
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        l = list(self.initial)
        random.shuffle(l)
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
