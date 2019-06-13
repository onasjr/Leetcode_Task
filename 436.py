## 寻找右区间
## 寻找首位大于末尾的项并更新
（超时）
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range(len(intervals)):
            tmp = -1
            ans = [float("inf"), float("inf")]
            for j in range(len(intervals)):
                if intervals[j][0] >= intervals[i][1]:  #起点>=终点
                    if ans[0] > intervals[j][0]:
                        ans = intervals[j]
                        tmp =  j
            res.append(tmp)
        return res
            
