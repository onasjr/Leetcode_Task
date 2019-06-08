## 递增的三元子序列
## a始终记录最小元素，b为子序列中次小元素，不断更新a和b，保持a<b的情况下更新，若能找到c比a，b大则True


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = float("inf")    # 存放最小值
        b = float("inf")    # 存放次小值
        for i in nums:
            if i <= a: 
                a = i
            elif i <= b:
                b = i
            else:       # 存在比a，b大一点的值
                return True
        return False        # 不存在c
