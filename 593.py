## 有效的正方形
## 计算四个点两两构成的距离，四个相同，剩余两个相同则T

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance(d1, d2):
            return (d1[0]-d2[0])**2+(d1[1]-d2[1])**2

        ans = []
        ans.append(distance(p1,p2))
        ans.append(distance(p1,p3))
        ans.append(distance(p1,p4))
        ans.append(distance(p2,p3))
        ans.append(distance(p2,p4))
        ans.append(distance(p3,p4))

        ans.sort()
        if ans[0] == ans[1] == ans[2] == ans[3] != 0 and ans[4] == ans[5] != 0:
            return True
        else:
            return False
