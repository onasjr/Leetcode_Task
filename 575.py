## 分糖果
## 计算实际的糖果种类，理论上可以得到的最大种类是len（candies）//2，比较大小

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        real = len(set(candies))
        pros = len(candies)//2
        if real < pros:
            return real
        else:
            return pros
