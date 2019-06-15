## 相对名次
## 先对nums从大到小排序，之后查找nums中数字在排序后的位置，赋值

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        A = []
        chain = sorted(nums, reverse = True)
        
        for i in nums:
            tmp = chain.index(i)
            if tmp == 0:
                A.append("Gold Medal")
            elif tmp == 1:
                A.append("Silver Medal")
            elif tmp == 2:
                A.append("Bronze Medal")
            else:
                A.append(str(tmp+1))
        return A
