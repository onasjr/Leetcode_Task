## 数组的度
## 遍历得到每个数字出现的次数，找出出现次数最多的数字，查找这些数字为首尾的子数组长度，输出最短数组

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 记录每个数字出现的次数
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        # 找到出现最多的数字
        maxnum = [i for i, v in dict.items() if v == max(dict.values())]

        minlen = len(nums)
        lll = len(nums)
        # 对每个数字查找以其为首尾的索引值
        for num in maxnum:
            for i in range(lll):
                if nums[i] == num:
                    start = i
                    break
            for i in range(lll - 1, -1, -1):
                if nums[i] == num:
                    end = i
                    break
            minlen = min(minlen, end-start+1)

        return minlen
