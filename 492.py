## 构造矩形
## 从开方值开始一次减一，计算可以整除的第一组数据


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        tmp = int(area**0.5)
        while area % tmp != 0:
            tmp -= 1
        
        return sorted([tmp, area//tmp], reverse = True)
