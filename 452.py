## 用最少数量的箭引爆气球
## 思路：求所有的交集，将数组按起始位排序，比较point[i][1]和res中暂存交集起始位是否相交，更新res


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points == [] or points == [[]]:
            return 0
        points.sort()
        res = [points[0]]
        for i in range(1, len(points)):
            if res[-1][1] >= points[i][0]:
                res[-1] = ([points[i][0], min(points[i][1], res[-1][1])])
            else:
                res.append(points[i])

        return len(res)
