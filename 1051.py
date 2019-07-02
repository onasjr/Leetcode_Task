## 高度检查器
#　对数组排序，统计排序前后数组不同位的个数

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        tmp = sorted(heights)
        for i in range(len(tmp)):
            if tmp[i] != heights[i]:
                ans += 1
        return ans
