## 合并区间
## 1.按每个区间第一个数大小排序
## 2.建立res保存合并后的区间，初始化res为区间第一个
## 3.比较区间起始和res末尾大小，若小于，则合并并替代res；否则添加



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res
