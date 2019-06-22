## 种花问题
## 分为前后2位和中间三位讨论，首尾都为0时可种花数+1，中间三个0时+1

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ll = len(flowerbed)
        if ll == 1:
            return 1-flowerbed[0] >= n
        count = 0
        if flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        for i in range(1, ll-1):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        if flowerbed[-1] == flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1
        return count >= n
