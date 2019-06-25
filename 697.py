## 数组的度
## 遍历得到每个数字出现的次数，找出出现次数最多的数字，查找这些数字为首尾的子数组长度，输出最短数组

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        tmp = list(set(nums))
        count = []
        for i in tmp:
            count.append(nums.count(i))

        maxcount = max(count)
        maxnum = []
        for i, v in enumerate(count):
            if v == maxcount:
                maxnum.append(tmp[i])

        minlen = len(nums)
        for num in maxnum:
            for i in range(len(nums)):
                if nums[i] == num:
                    start = i
                    break
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == num:
                    end = i
                    break
            minlen = min(minlen, len(nums[start:end + 1]))

        return minlen
