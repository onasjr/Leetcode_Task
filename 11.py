# 盛水最多的容器
## 思路：双指针法：在头尾处设置两个index，计算由短边确定的矩形面积，计算出结果后使短边向长边方向移动1

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        num = len(height)
        index1 = 0
        index2 = num - 1
        while index1 < index2:
            area = max(area, (index2 - index1) * min(height[index1], height[index2]))
            if height[index1] > height[index2]:
                index2 -= 1
            else:
                index1 += 1
        return area
