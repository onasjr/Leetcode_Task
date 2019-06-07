## 建立dict保存某个距离的出现个数


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dict = {} # 存储某个距离出现的次数
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j :
                    distance = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                    if distance in dict:
                        res += 2 * dict[distance]
                        dict[distance] += 1
                    else:
                        dict[distance] = 1
            dict = {}
        return res
