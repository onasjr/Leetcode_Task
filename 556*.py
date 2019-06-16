## 下一个更大元素 III
## 从右往左遍历，找到第一个比右边数字小的， 从这个数开始从右往左找到第一个比它大的数字
## 交换这两位，并对小数右边部分排序得到最小

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(x) for x in str(n)]
        if sorted(nums)[::-1] == nums:
            return -1
        m = len(nums)
        
        ## 从右往左遍历，找到第一个比右边数字小的
        for i in range(m - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ## 从这个数开始从右往左找到第一个比它大的数字
                for j in range(m - 1, i, -1):
                    if nums[j] > nums[i]:
                        ## 交换这两位，并对小数右边部分排序得到最小
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        break
                break
        res = 0
        for i in nums:
            res = 10 * res + i
        return res if res<2**31 else -1
