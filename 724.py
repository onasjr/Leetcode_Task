## 寻找数组的中心索引
## 计算截止到第i位的数字和，遍历，比较前后数字和是否相等；
## 特殊情况：[]， 首位后为0， 末位前为0

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        if sum(nums[1:]) == 0:
            return 0
        sumline = []
        sums = 0

        for i in range(len(nums)):
            sums += nums[i]
            sumline.append(sums)

        for i in range(1,len(sumline)):
            if sumline[i-1] == sumline[-1]-sumline[i]:
                return i

        if sum(nums[:-1]) == 0:
            return len(nums)-1
        else:return -1
