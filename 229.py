## 求众数 II
## dict，遍历
## 空间复杂度高

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)//3
        tmp = {}
        res = []
        
        for i in nums:
            if i in tmp.keys():
                tmp[i] += 1
            else:
                tmp[i] = 1
        
        [res.append(i) for i in tmp.keys() if tmp[i] > length]
        return res
