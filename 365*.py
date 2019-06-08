## 水壶问题
## 找到x,y的最大公约数能否z被整除

class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x+y < z:   # 如果水壶总和<z
            return False
        if x>y:
            x,y=y,x   # 另x<y
        if x == 0:
            return y==z
        while y%x != 0:
            y,x = x,y%x
        return z%x==0
