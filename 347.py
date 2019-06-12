## 前k个高频元素
## dict存储出现的字符及次数
## 对dict中value排序，获取最大k个的key


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        return sorted(dict.keys(), key= dict.get, reverse= True)[:k]
